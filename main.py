#import routes
from flask import Flask, request, make_response, send_from_directory, jsonify, redirect, url_for, render_template
from flask_session import Session
import json
#from flask_sqlalchemy import SQLAlchemy

from database import *
#from pathlib import Path
app = Flask(__name__, template_folder="../client/templates", static_folder="../client/static")

# --- loads config.json
config_file = open("./config.json")
config = json.load(config_file)
# ---

app.config['SQLALCHEMY_DATABASE_URI'] = config["database"]["uri"]
db = SQLAlchemy(app)
#db = declarative_base(app)

app.config['SECRET_KEY'] = config["secret_key"]
sess = Session(app)

from routes import *
        
# --- runs the app
if __name__ == "__main__":
    app.run(host = config["socket"]["ip"], port = config["socket"]["port"])
# ---