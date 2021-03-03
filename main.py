#import routes
from flask import Flask
from flask_session import Session as Sess
import json
#from flask_sqlalchemy import SQLAlchemy
from database import *

#from pathlib import Path
app = Flask(__name__, template_folder="../client/templates", static_folder="../client/static")

# --- loads config.json
config_file = open("./config.json")
config_server = json.load(config_file)
# ---
app.config['SQLALCHEMY_DATABASE_URI'] = config_server["database"]["uri"]
app.config['SESSION_TYPE'] = "sqlalchemy"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
app.config['SESSION_SQLALCHEMY'] = db

app.config['SECRET_KEY'] = config_server["secret_key"]
Sess(app)
db.create_all()

from routes import *
        
# --- runs the app
if __name__ == "__main__":
    app.run(host = config_server["socket"]["ip"], port = config_server["socket"]["port"])
# ---