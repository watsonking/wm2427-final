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
@app.route("/semester")
def course():
    return render_template("semester.html")
@app.route("/identity")
def tp():
    return render_template("African.html")
@app.route("/love")
def lp():
    return render_template("Oldpoem.html")
 


#start the server
if __name__ == "__main__":
    app.run()