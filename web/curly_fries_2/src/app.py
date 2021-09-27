from flask import Flask, request, render_template

app = Flask(__name__,
            static_url_path='',
            template_folder='')
app.secret_key = 'qwertyQWERTY'

@app.route('/')
def home():
  user_agent = request.user_agent.string.lower()
  x = 'xbox' in user_agent
  l = 'linux' in user_agent
  if not x and not l:
    return render_template('xl.html')
  elif x and not l:
    return render_template('l.html')
  elif not x and l:
    return render_template('x.html')
  else:
    return render_template('poppycock.html')
