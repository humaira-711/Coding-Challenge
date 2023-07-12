from flask import Flask, request, render_template, redirect
import pickle
import numpy as np
from datetime import datetime
import json
import base64
from io import BytesIO
import mysql.connector

# Establish a connection to the database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="regov"
)

app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])
def home():
    return render_template('register.html')

@app.route("/viewlogin", methods = ['GET','POST'])
def viewlogin():
    return render_template('login.html') 

@app.route("/viewUser",methods = ['GET','POST'])
def viewUser():
    return render_template('profile.html') 

@app.route("/insert_data", methods=['GET','POST'])
def insert_data():
    cursor = db.cursor()
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    query = "INSERT INTO user (name, email, password) VALUES (%s, %s, %s)"
    values = (name, email, password)
    cursor.execute(query, values)
    db.commit()
    return "Data inserted successfully"


if __name__ == "__main__":
    app.run(debug = True)