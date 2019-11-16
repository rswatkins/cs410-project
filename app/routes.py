from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/parameters')
def parameters():
    return render_template('parameters.html')
