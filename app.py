from flask import render_template, jsonify
from InfrastructureLayer.DBconfig import DatabaseConfig
import os

app = DatabaseConfig()


@app.route('/')
def index():
    return jsonify('Welcome to the Software Design Project: Baggage Handling System')


if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(debug=True)
