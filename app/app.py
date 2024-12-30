from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    deployment_env = os.getenv('DEPLOYMENT_ENV', 'Unknown')
    return f"<h1>Welcome to the {deployment_env} Deployment!</h1><p>This is the home page of the Flask app.</p>"

@app.route('/about')
def about():
    return "<h1>About Page</h1><p>This is a simple Flask application example.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
