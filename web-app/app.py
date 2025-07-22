from flask import Flask, request, render_template_string
import logging
from datetime import datetime

app = Flask(__name__)

# Set up logging
logging.basicConfig(filename='/app/app.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Function to detect suspicious path
def is_suspicious(path):
    return '../' in path or 'etc' in path or 'shadow' in path

# --------------------
# Normal Access
# --------------------
@app.route('/')
def home():
    client_ip = request.remote_addr
    log_message = f"Normal access: / - IP: {client_ip}"
    app.logger.info(log_message)
    return "<h2>Welcome to the Flask Web App!</h2><p>This is the home page.</p>"

# --------------------
# Admin Access
# --------------------
@app.route('/admin')
def admin():
    client_ip = request.remote_addr
    log_message = f"Admin access: /admin - IP: {client_ip}"
    app.logger.info(log_message)
    return "<h2>Admin Page</h2><p>You have accessed the admin section.</p>"

# --------------------
# Catch-all for Suspicious or Other Paths
# --------------------
@app.route('/<path:path>')
def catch_all(path):
    client_ip = request.remote_addr
    full_path = '/' + path

    if is_suspicious(full_path):
        log_message = f"🚨 Suspicious path accessed: {full_path} - IP: {client_ip}"
        app.logger.warning(log_message)
        return render_template_string("""
            <html>
                <head><title>Suspicious Access</title></head>
                <body>
                    <script>alert("⚠️ Suspicious activity detected! Your request has been logged.");</script>
                    <h2>Suspicious Request Detected!</h2>
                    <p>The path you tried to access looks suspicious and has been logged.</p>
                </body>
            </html>
        """)
    else:
        log_message = f"Unknown path accessed: {full_path} - IP: {client_ip}"
        app.logger.info(log_message)
        return f"<h2>Unknown Path</h2><p>You accessed: {full_path}</p>"

# --------------------
# Run the Flask App
# --------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
