from flask import Flask 
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    name = "Caleb's"

    return render_template('new_index.html', name=name)

if __name__ == "__main__":
    app.run()
