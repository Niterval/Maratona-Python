from flask import Flask, render_template, request



app = Flask('SMS_Rastreio')

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/result")
def reuslt():


    return render_template('result.html')






















app.run()