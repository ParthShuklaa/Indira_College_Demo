import  flask
from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/")
def show():
    return "<h1>Hello World</h1>"
@app.route("/index")
def Msg():
    return ("Welcome to Index page.....")
@app.route('/DemoFlask')
def Message():
    return render_template('DemoFlask.html')
app.run()
