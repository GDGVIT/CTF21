from flask import Flask,render_template,send_from_directory,request,g
import mysql.connector
import os


def get_db():
    db = getattr(g,'_database',None)
    if db is None:
        db = g._database = mysql.connector.connect(
                host=os.environ.get("SQL_HOST"),
                port=os.environ.get("SQL_PORT"),
                user=os.environ.get("SQL_USER"),
                password=os.environ.get("SQL_PASSWORD"),
                database=os.environ.get("SQL_DATABASE"))
    return db

def query_db(query, args=(), one=False):
    cur = get_db().cursor(buffered=True)
    cur.execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def query_page():

    error = False
    no_value = False
    if request.method == "POST":
        lisence_plate = request.form.get("lisence_plate")
        try:
            taxi = query_db("SELECT lisence_plate,driver_name,ph_no FROM taxi WHERE lisence_plate = '{}'".format(lisence_plate))
        except mysql.connector.errors.ProgrammingError as e:
            print(e)
            error = True
            return render_template("taxi_info.html",error=error)

        if taxi == []:
            no_value = True
            return render_template("taxi_info.html",no_value=no_value)
        else:
            return render_template("taxi_info.html",taxi=taxi)
    else:
        return render_template("taxi_info.html")

if __name__ == "__main__":
    app.run()
