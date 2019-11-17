import os
from app import app
from flask import render_template, request

app.config["UPLOAD_FOLDER"] = app.root_path + "/static/spreadsheets"

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

@app.route('/upload', methods = ['POST'])
def upload():
    if request.method == 'POST':
        spreadsheet = request.files['myFile']
        spreadsheet.save(os.path.join(app.config["UPLOAD_FOLDER"],spreadsheet.filename))
        return render_template('index.html')
