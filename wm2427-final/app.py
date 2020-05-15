# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:57:17 2020

@author: etill
"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    return render_template("index.html")
@app.route("/1006")
def course():
    return render_template("columbia.html")
@app.route("/semester")
def columbia():
    return render_template("semester.html")
@app.route("/tester")
def tester1():
    return render_template("index1.html")
 


#start the server
if __name__ == "__main__":
    app.run()