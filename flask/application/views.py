from application import app
import os

@app.route("/")
def index():
    app_name = os.getenv("APP_NAME")
    if app_name:
        return f"Hello from {app_name} running in a Docker container behind a Nginx"
    return "Hello from Flask"
