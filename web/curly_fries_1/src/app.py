from flask import Flask, request, render_template

app = Flask(__name__,
            static_url_path='',
            static_folder='assets',
            template_folder='')
app.secret_key = 'qwertyQWERTY'

@app.route('/')
def home():
  language = request.headers.get('Accept-Language')
  if language and 'sv-SE' in language:
    return 'dsc{1_l0v3_sw3d3n}'
  return render_template('sweden.html')
