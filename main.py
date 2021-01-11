#import routes
from flask import Flask, request, make_response, send_from_directory, jsonify

import json
from database import *
#from pathlib import Path
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/fakedb'
db = SQLAlchemy(app)

# --- loads config.json
config_file = open("./config.json")
config = json.load(config_file)
# ---

from routes import *

# @app.route("/test/", methods = ["GET"])
# def test():
#     if request.method == "GET":
#         print(request.headers)
#         return str(request.headers) + "<br><br><br>Server runs successfully(maybe). Atleast it can serve this /test"

# @app.route("/", methods = ["GET"])
# def landing():
#     if request.method == "GET":
#         return "landing page"
#         #return send_from_directory("../fakeclient/", "index.html")
#     # return render_template("index.html")
    
# @app.route("/signup/", methods = ["GET", "POST"])
# def signup():
#     if request.method == "GET":
#         return send_from_directory("../fakeclient/", "index.html")
#     elif request.method == "POST":
#         print(request.form)
#         return "done"
        
        
        
# --- runs the app
if __name__ == "__main__":
    app.run(host = config["socket"]["ip"], port = config["socket"]["port"])
# ---