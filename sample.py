from flask import Flask

app = Flask(__name__)  # Create a Flask application

@app.route('/')  # Define route for home page
def home():
    return "Hello, Flask!"  # Response shown on visiting "/"

if __name__ == '__main__':
    app.run(debug=True)  # Run the server
