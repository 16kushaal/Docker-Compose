from flask import Flask
import requests
app = Flask(__name__)
@app.route('/')
def hello():
    try:
        # Make a request to Service 2
        response = requests.get('http://service1:5000')
        return f"Service 1 get response: {response.text}"
    except Exception as e:
        return f"Failed to connect to Service 1: {e}"

if __name__ == '_main_':
    app.run(host='0.0.0.0', port=5001, debug=True)