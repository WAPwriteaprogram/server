#import routes
from flask import Flask, request, make_response, send_from_directory, jsonify, redirect, url_for
import json
from database import *
#from pathlib import Path
app = Flask(__name__)

# --- loads config.json
config_file = open("./config.json")
config = json.load(config_file)
# ---

app.config['SQLALCHEMY_DATABASE_URI'] = config["database"]["uri"]
db = SQLAlchemy(app)

from routes import *
        
# --- runs the app
if __name__ == "__main__":
    app.run(host = config["socket"]["ip"], port = config["socket"]["port"])
# ---