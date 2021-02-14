#from flask import Flask, request, make_response, send_from_directory, jsonify
from main import *
from passlib.hash import pbkdf2_sha256
#app = Flask(__name__)

@app.route("/test/", methods = ["GET"])
def test():
    if request.method == "GET":
        print(request.headers)
        return str(request.headers) + "<br><br><br>Server runs successfully(maybe). Atleast it can serve this /test"

@app.errorhandler(500)
def error(e):
    print(e)
    return "Please contact MEC administrator"

@app.route("/", methods = ["GET"])
def landing():
    if request.method == "GET":
        #return send_from_directory("../client/Html/Pages/", "landingPage.html")
        return render_template("landingPage.html")
    
@app.route("/signup/", methods = ["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("auth/signup.html")
        
    elif request.method == "POST":
        #print(request.form)
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        password_hashed = pbkdf2_sha256.hash(password)
        
        user_object = User.query.filter_by(email=email).first()
        if user_object is not None:
            return "email taken"
            
        user_object = User.query.filter_by(username=username).first()
        if user_object is not None:
            return "username taken"
        
        user = User(username=username, email=email, password_hashed=password_hashed, privilage=0)
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for("login"))
        
@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("auth/login.html")
    
    elif request.method == "POST":
        username = request.form["username"]
        password_entered = request.form["password"]
        
        user_object = User.query.filter_by(username=username).first()
        if user_object is None:
            return "username invalid"
        elif not pbkdf2_sha256.verify(password_entered, user_object.password_hashed):
            return "wrong password"
        else:
            return f"welcome {username}"
            
@app.route("/home/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")
