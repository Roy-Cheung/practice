from flask import Flask     #keep remind that import Flask is a capital letter
from flask import request   
from flask import render_template   #used to rediect to the template folder


app=Flask(__name__, static_folder="public",static_url_path="/")

# the function of the corresponding route
@app.route("/")
def index():
    return render_template("index.html")

app.run()