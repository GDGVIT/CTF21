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

@app.route("/")
def home_page():
    return render_template("startbootstrap-scrolling-nav-gh-pages/index.html")

@app.route("/robots.txt")
def robots():
    return send_from_directory('static','robots.txt')

@app.route("/never_gonna_give_you_up")
def admin_login():
    return render_template("admin_page/index.html")

@app.route("/never_gonna_let_you_down",methods=['POST'])
def admin_login_post():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        try:
            user = query_db("SELECT * FROM users WHERE username = '{}' AND password = '{}'".format(username,password))
        except:
            user = None
        if user == None:
            return "YOU LIED TO ME !!!\n"
        else:
            return "dsc{7H15_15_93771N9_0Ld}"

if __name__ == "__main__":
    app.run()
