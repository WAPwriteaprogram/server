#from flask import Flask, request, make_response, send_from_directory, jsonify
from main import *

#app = Flask(__name__)

@app.route("/test/", methods = ["GET"])
def test():
    if request.method == "GET":
        print(request.headers)
        return str(request.headers) + "<br><br><br>Server runs successfully(maybe). Atleast it can serve this /test"

@app.route("/", methods = ["GET"])
def landing():
    if request.method == "GET":
        return "landing page"
        #return send_from_directory("../fakeclient/", "index.html")
    # return render_template("index.html")
    
@app.route("/signup/", methods = ["GET", "POST"])
def signup():
    if request.method == "GET":
        return send_from_directory("../fakeclient/", "index.html")
    elif request.method == "POST":
        #print(request.form)
        email = request.form["mail"]
        password = request.form["passw"]
        
        user_object = User.query.filter_by(email=email).first()
        if user_object is not None:
            return "email taken"
        
        user = User(email=email, password=password)
        db.session.add(user)
        db.session.commit()
        
        return "done"
        