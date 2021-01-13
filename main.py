#import routes
from flask import Flask, request, make_response, send_from_directory, jsonify, redirect, url_for
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
        
# --- runs the app
if __name__ == "__main__":
    app.run(host = config["socket"]["ip"], port = config["socket"]["port"])
# ---