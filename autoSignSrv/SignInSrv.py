from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/SignIn",methods = ['GET','POST'])
def SignIn():
    print(request.args)
    print(request.form)
    print(request.values)
    print(type(request.data) )

    print(request)
    return "hello"
