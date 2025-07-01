from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    log_request("Normal access")
    return "Hello, World!"

@app.route('/admin', methods=['GET'])
def admin():
    log_request("Admin area accessed")
    return "This is the admin page!"

@app.route('/login', methods=['POST'])
def login():
    log_request("Login attempt")
    return "Login route"

@app.route('/<path:invalid_path>')
def catch_all(invalid_path):
    log_request(f"Invalid path accessed: /{invalid_path}")
    return "404 Not Found", 404

def log_request(event):
    with open("/app/app.log", "a") as f:
        f.write(f"{datetime.datetime.now()} - {event} - IP: {request.remote_addr}\n")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
