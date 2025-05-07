from flask import Flask
import requests
app = Flask(__name__)
@app.route('/')
def hello():
    try:
        # Make a request to Service 2
        response = requests.get('http://service2:5001')
        return f"Service 2 get response: {response.text}"
    except Exception as e:
        return f"Failed to connect to Service 2: {e}"

if __name__ == '_main_':
    app.run(host='0.0.0.0', port=5000, debug=True)