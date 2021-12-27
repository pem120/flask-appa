import os
# checking if flask is installed else installing flask
try:
    import flask
except:
    os.system("pip3 install flask")
    import flask
from flask import *

# makeing the app
app = Flask(__name__)


# home page
@app.route("/")
def home():
    retrun "hello"
if  __name__ == "__main__":
    app.run()
