#import routes
from flask import Flask, request, make_response, send_from_directory, jsonify, redirect, url_for, render_template, session
from flask_session import Session as Sess
import json
from flask_sqlalchemy import SQLAlchemy

from database import *
#from pathlib import Path
app = Flask(__name__, template_folder="../client/templates", static_folder="../client/static")

# --- loads config.json
config_file = open("./config.json")
config = json.load(config_file)
# ---

db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = config["database"]["uri"]
app.config['SESSION_TYPE'] = "sqlalchemy"
app.config['SESSION_SQLALCHEMY'] = db
#db = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

app.config['SECRET_KEY'] = config["secret_key"]
Sess(app)
#db.create_all()

from routes import *
        
# --- runs the app
if __name__ == "__main__":
    app.run(host = config["socket"]["ip"], port = config["socket"]["port"])
# ---