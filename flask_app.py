
# A very simple Flask Hello World app for you to get started with...
import os
from flask import send_from_directory
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Meu primeiro Site no flask localmente!</h1>'

@app.route('/home')
def inicio():
    icone = url_for ('static', filename='peter')
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
    'favicon.ico', mimetype='img/peter.png')