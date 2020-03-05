
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='icone.png')


@app.route('/')
def hello_world():
    return '<h1>Meu primeiro Site no flask localmente!</h1>'

@app.route('/inicio')
def inicio():
    return render_template('index.html')

