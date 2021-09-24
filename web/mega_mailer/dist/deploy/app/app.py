import csv
import io
from smtplib import SMTP
from flask import Flask,render_template,send_from_directory,request,g,make_response
from jinja2 import Template
import os

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def Mailer():
    error = False
    no_value = False
    if request.method == "POST":
        uploaded_file = request.files['recipitents']
        smtp_server = request.form.get("smtp_host")
        smtp_port = request.form.get("smtp_port")
        from_addr = request.form.get("from_addr")
        body = request.form.get("body")
        recipient_data = csv.DictReader(io.StringIO(uploaded_file.read().decode()))
        with SMTP(smtp_server,smtp_port) as smtp:
            template = Template(body)
            for data in recipient_data:
                body_html = template.render(data)
                smtp.sendmail(from_addr,data["email"],body_html)
            return render_template('home.html',success=True)
    else:
        return render_template('home.html')

            
if __name__ == "__main__":
    app.run(debug=True)
