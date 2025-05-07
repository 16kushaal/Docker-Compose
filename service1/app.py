from flask import Flask
import requests

app =Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Service 1!"

if __name__=="main_":
        app.run(host='0.0.0.0', port =5000, debug=True)