from flask import Flask, request
from flask.helpers import make_response

app = Flask(__name__)
app.secret_key = 'qwertyQWERTY'

@app.route('/', methods=['POST'])
def home():
  referer = request.headers.get('Referer')
  if not referer or (referer and 'https://www.google.com' not in referer):
    return 'perhaps try Googling me instead?'

  host = request.headers.get('Host')
  if not host or (host and 'dscvit' not in host):
    return 'did you attend that lovely dinner party Hosted by dscvit?'

  cookie_hint = 'potates and carrots are my friends, milk and Cookies will be my end'
  resp = make_response(cookie_hint)
  resp.set_cookie('user', 'anon')
  user = request.cookies.get('user')
  if user != 'root':
    return resp

  content_type = request.headers.get('Content-Type')
  if not content_type or (content_type and 'application/json' not in content_type.lower()):
    return 'JFATHER, JMOTHER, JDAUGHTER, ____?'

  json = request.get_json(silent=True)
  if json == None:
    return "{'error': 'json data missing'}"
  if not json.get('messi'):
    return "{'error': {'messi': 'required'}}"
  print (json['messi'])
  if 'psg' not in json['messi'].lower() and 'paris' not in json['messi'].lower():
    return "{'error': {'messi': 'which club am i at?'}}"

  return 'Congrats! The flag is dsc{th15_15_w4y_t00_much_w0rk}'

# curl -v -H 'Referer: https://www.google.com' -H 'Host: dscvit.com' -b user=root -H 'Content-Type: application/json' --data '{"messi":"psg"}' -X POST http://127.0.0.1:5000
