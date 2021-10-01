from flask import Flask, request, make_response
from flask.templating import render_template

app = Flask(__name__)
app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
)

@app.route('/', methods=['GET'])
def home():
    resp = make_response(render_template('index.html'))
    resp.headers['X-XSS-Protection'] = '1; mode=block'
    resp.set_cookie('flag=c29tZXRpbWVzIHRoZSBrZXkgdG8gdW5sb2NraW5nIHRoZSBhbnN3ZXIgaXMgdGhlIHF1ZXN0aW9uIGl0c2VsZi4uLiBidXQgbXkgZmF2b3JpdGUgaXMgY2hvY28gY2hpcA== ')
    resp.delete_cookie('flag')
    param_cookie = request.cookies.get("flag")
    if param_cookie=='c29tZXRpbWVzIHRoZSBrZXkgdG8gdW5sb2NraW5nIHRoZSBhbnN3ZXIgaXMgdGhlIHF1ZXN0aW9uIGl0c2VsZi4uLiBidXQgbXkgZmF2b3JpdGUgaXMgY2hvY28gY2hpcA==':
        return {"flag":"522748524ad010358705b6852b81be4c"}

    elif param_cookie=='522748524ad010358705b6852b81be4c':
        return {"flag":"70e9490b5d5a217070c1e7df9518e9d5"}

    elif param_cookie=='70e9490b5d5a217070c1e7df9518e9d5':
        return {"flag":"60173ca988f93d0a7da64f3327ad336c"}

    elif param_cookie=='60173ca988f93d0a7da64f3327ad336c':
        return {"flag":"45ec864b6976a208c6af1a37e2c61c3a"}

    elif param_cookie=='45ec864b6976a208c6af1a37e2c61c3a':
        return {"flag":"046bf0a7d0d641c527765a02816eca9f"}

    elif param_cookie=='046bf0a7d0d641c527765a02816eca9f':
        return {"flag":"24cafc74b88dfafb0524ecc85a76f8bd"}

    elif param_cookie=='24cafc74b88dfafb0524ecc85a76f8bd':
        return {"flag":"f3ea97d2cd1f5619f570c06a10a041b5"}

    elif param_cookie=='f3ea97d2cd1f5619f570c06a10a041b5':
        return {"flag":"fa4f4d80f554c6845daf73511d75e6bc"}

    elif param_cookie=='fa4f4d80f554c6845daf73511d75e6bc':
        return {"flag":"72e6f6e0f08ca88f02b1480464afd55b"}

    elif param_cookie=='72e6f6e0f08ca88f02b1480464afd55b':
        return {"flag":"97d243cd9c2513d20fff6d5677b2b62b"}

    elif param_cookie=='97d243cd9c2513d20fff6d5677b2b62b':
        return {"flag":"ffc987113c7a22fb2a52b6f9842f79be"}

    elif param_cookie=='ffc987113c7a22fb2a52b6f9842f79be':
        return {"flag":"a61c8204ca3eb98c9da7344cf0fba066"}

    elif param_cookie=='a61c8204ca3eb98c9da7344cf0fba066':
        return {"flag":"9bea76c2f9cb9140f837ee4518b6749c"}

    elif param_cookie=='9bea76c2f9cb9140f837ee4518b6749c':
        return {"flag":"EOF"}
    
    return resp

if __name__ == '__main__':
    app.run(debug=False)