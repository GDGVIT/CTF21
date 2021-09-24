from flask import Flask,render_template,url_for,redirect
import os

app = Flask(__name__)

@app.route("/",methods=['GET'])
def download_page():
    return render_template("home.html")   

@app.route("/display",methods=['GET'])
def display_video():
    return redirect(url_for('static', filename='uploads/flag.mp4'), code=301)

if __name__ == "__main__":
    app.run()
