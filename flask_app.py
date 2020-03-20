
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_templates

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Meu primeiro Site no flask localmente!</h1>'

@app.route('/home')
def inicio():
    return render_templates('index.html')

