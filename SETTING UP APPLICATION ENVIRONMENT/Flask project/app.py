# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 13:44:20 2022

@author: Rithiha
"""

from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def display():
    return render_template("display.html")
@app.route('/home')
def home():
    return "Hello world"
if __name__==('__main__'):
    app.run(debug=True)
