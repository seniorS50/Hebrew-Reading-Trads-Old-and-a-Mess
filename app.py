import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
import time
import json

app = Flask(__name__)

@app.route("/")
def index():
    with open('FileNames.json') as f:
        data = json.load(f)

    ##city = input("Which city?")

    return render_template("index.html", entry=data)


@app.route("/search", methods = ['GET'])
def search():
    with open('FileNames.json') as f:
        data = json.load(f)

    ##city = input("Which city?")
    if request.args:
        data = request.args["arg1"]

    return render_template("index.html", entry="")