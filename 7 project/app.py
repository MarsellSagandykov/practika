import codecs
import subprocess
import os
from flask import Flask, render_template, request, flash, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/analysis')
def analysis():
    return render_template('analysis.html')


@app.route('/extract', methods=["post"])
def extract():
    txt0 = request.form['txt']
    with codecs.open('./test.txt', 'w', 'utf-8') as f:
        f.write(str(txt0))
    command = ['./tomitaparser', 'config.proto']
    output = subprocess.check_output(command)
    return render_template('pretty.html')

if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0', port = 5001)