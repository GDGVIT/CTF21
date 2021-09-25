from flask import Flask,render_template,send_from_directory,request,g
import sqlite3
import os


def get_db():
    db = getattr(g,'_database',None)
    directory = os.getcwd()
    uri = f'file:/{directory}/database.db?mode=ro'
    print(uri)
    if db is None:
        db = g._database = sqlite3.connect(uri, uri=True)
    return db

def query_db(query, args=(), one=False):
    cur = get_db().cursor()
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
        password = request.form.get("password")
        try:
            taxi = query_db("SELECT password FROM passwords WHERE password = '{}'".format(password))
        except Exception as e :
            print(e)
            error = True
            return render_template("gate_keeper.html",error=error)

        if taxi == []:
            no_value = True
            return render_template("gate_keeper.html",no_value=no_value)
        else:
            return render_template("gate_keeper.html",value=True)
    else:
        return render_template("gate_keeper.html")

if __name__ == "__main__":
    app.run()
