#!/usr/bin/python
from flask import Flask 
from flask import render_template

app = Flask(__name__)

@app.route("/")
def landingPage():
        
    return render_template('new_index.html')

@app.route("/coaching")
def coaching():
    
    user = "Kamic0"
    return render_template('index.html', user=user)

if __name__ == "__main__":
    app.run(debug=True)


