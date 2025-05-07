from flask import Flask
import requests

app =Flask(__name__)

@app.route('/')
def hello():
    try:
        response = requests.get("http://service1:5000")
        return f"Service 2 got response:{response.text}"
    except Exception as e:
        return f"Failed to connect to service1: {e}"
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)