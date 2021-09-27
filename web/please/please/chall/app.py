from flask import Flask, request, make_response
from flask.templating import render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def loginpage():
    resp = make_response(render_template('home.html'))
    resp.set_cookie('Username', "Unknown")
    resp.set_cookie('Admin_Access', "False")
    return resp


@app.route('/dashboard', methods=['POST', 'GET'])
def setcookie():
    try:
        username = request.args['uname']
    except:
        username = request.cookies.get('Username')
    admin_access = request.cookies.get('Admin_Access')

    if username != "Clancy":
        resp = make_response(
            render_template('dashboard.html',
                            bigdisplay="Hello!",
                            display="Hello "+username+"! We're sorry for the inconvenience but only Clancy can access this website at the moment."))
        resp.set_cookie("Username", username)
        return resp
    else:
        if admin_access == "False":
            resp = make_response(render_template('dashboard.html',
                                                 bigdisplay="Error!",
                                                 display="Hello "+username+"! We're sorry, but only administrators can access this page!"))
            return resp
        else:
            if request.headers['User-Agent'] != "DeemaBrowser":
                resp = make_response(render_template('dashboard.html',
                                                     bigdisplay="Error!",
                                                     display="Hello "+username+"! All admins are required to use the special\
                            <b>DeemaBrowser</b> to access the admin page. Please switch your browser from "+request.headers['User-Agent']+" to DeemaBrowser\
                                to continue"))
                return resp
            else:
                try:
                    auth = request.headers['Authorization']
                except:
                    auth = None
                if auth == None:
                    resp = make_response(render_template('dashboard.html',
                                                         bigdisplay="Error!",
                                                         display="Hello "+username+"! Basic Authorization not provided. Please provide\
                                                         a Basic Authorization with the passphrase \"What'sTheMagicWord?\""))
                    return resp
                elif auth != "Basic V2hhdCdzVGhlTWFnaWNXb3JkPw==":
                    resp = make_response(render_template('dashboard.html',
                                                         bigdisplay="Error!",
                                                         display="Hello "+username+"! Wrong Authorization! Please provide\
                                                         a Basic Authorization with the plaintext passphrase \"What'sTheMagicWord?\""))
                    return resp
                else:
                    try:
                        date = request.headers['Date']
                    except:
                        date = None
                    if date == None:
                        resp = make_response(render_template('dashboard.html',
                                                             bigdisplay="Error!",
                                                             display="Hello "+username+"! This file was only accessible in April of 2021.\
                                                             Today's current date hasn't been provided, so access has been blocked!"))
                        return resp
                    elif date != "Mon, 5 Apr 2021 12:00:00 GMT" and date != "Mon, 05 Apr 2021 12:00:00 GMT":
                        resp = make_response(render_template('dashboard.html',
                                                             bigdisplay="Error!",
                                                             display="Hello "+username+"! This file was only accessible on Monday, 5th April 2021, at 12:00:00 GMT. \
                                                             Unless you have a time machine, access has been blocked"))
                        return resp
                    else:
                        resp = make_response(render_template('dashboard.html',
                                                             bigdisplay="Good Job!",
                                                             display="Hello "+username+"! Here's your file: dsc{4ll-y0u-g0tt4-d0-15-r3qu35t-n1c3ly}"))
                        return resp


if __name__ == '__main__':
    app.run()
