from flask import Flask
from flask import render_template
from flask import request
from model import predict

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')