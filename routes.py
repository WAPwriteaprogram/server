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
        
        #user_object = User.query.filter_by(email=email).first()
        user_object = User.query.filter_by(email=email).first()
        if user_object is not None:
            return "email taken"
            
        user_object = User.query.filter_by(username=username).first()
        if user_object is not None:
            return "username taken"
        
        user = User(username=username, email=email, password_hashed=password_hashed, privilege=0)
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
            session["username_sess"] = username
            session["password_hashed_sess"] = password_entered
            session["privilege_sess"] = user_object.privilege
            return f"welcome {session.get('username_sess')}"
            
@app.route("/home/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return f"welcome {session.get('username_sess')}"
        #return render_template("home.html")

@app.route("/api/<query>", methods=["GET", "POST"])
def api(query):
    user_object = User.query.filter_by(username=session.get("username_sess")).first()
    #print(user_object.batch)
    if user_object is None:
        return "No session detected"
    elif not pbkdf2_sha256.verify(session.get("password_hashed_sess"), user_object.password_hashed):
        return "Dont try this. We are logging your activity"
    else:
        if query == "user" and request.method == "GET":
            return jsonify(
                username=user_object.username,
                email=user_object.email,
                privilege=user_object.privilege,
                courses_joined=user_object.courses_joined
            )
        if query == "add_course" and request.method == "POST":
            if session.get("privilege_sess") == 0:
                return "Requires admin/instructor privilege"
                
            add_course_json = request.get_json(force=True)
            users_object = User.query.filter_by(batch=add_course_json["batch"], section=add_course_json["section"]).all()
            
            course = Course(
                course_code=add_course_json["course_code"],
                course_name=add_course_json["course_name"],
                students=add_course_json["students"],
                instructors=add_course_json["instructors"]
            )
            db.session.add(course)
            db.session.commit()
            return f"{add_course_json['students']}"
        else:
            return "Check API query again"