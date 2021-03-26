from flask import request, make_response, send_from_directory, jsonify, redirect, url_for, render_template, session
from main import *
from passlib.hash import pbkdf2_sha256
import re

@app.route("/test/", methods = ["GET"])
def test():
    print(request.headers)
    return str(request.headers) + "<br><br><br>Server runs successfully(maybe). Atleast it can serve this /test"

@app.errorhandler(500)
def error(e):
    print(e)
    return "Please contact MEC administrator"

@app.route("/", methods = ["GET"])
def landing():
    #return send_from_directory("../client/Html/Pages/", "landingPage.html")
    return render_template("landingPage.html")
    
@app.route("/signup/", methods = ["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("auth/signup.html")
        
    #print(request.form)
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]
    password_hashed = pbkdf2_sha256.hash(password)
    
    if not re.match("^[A-Za-z0-9]+$", username):
        return "invalid username characters. Only letters and 0-9 allowed"
		
    user_object = User.query.filter_by(email=email).first()
    if user_object is not None:
        return "email taken"
    user_object = User.query.filter_by(username=username).first()
    if user_object is not None:
        return "username taken"
    
    user = User(username=username, email=email, password_hashed=password_hashed, privilege=2)
    db.session.add(user)
    db.session.commit()
        
    return redirect(url_for("login"))
        
@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("auth/login.html")
    
    else:
        try:
            username = request.form["username"]
            password_entered = request.form["password"]
        except:
            return "Invalod POST request"
            
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
            
@app.route("/home/", methods=["GET"])
def home():
    return f"welcome {session.get('username_sess')}"
    #return render_template("home.html")

@app.route("/api/<query>", methods=["GET"])
def api_get(query):
    user_object = User.query.filter_by(username=session.get("username_sess")).first()
    #print(user_object.batch)
    if user_object is None:
        return "No session detected"
    elif not pbkdf2_sha256.verify(session.get("password_hashed_sess"), user_object.password_hashed):
        return "Invalid password. We are logging your activity"
    else:
        if query == "user":
            return jsonify(
                username=user_object.username,
                email=user_object.email,
                privilege=user_object.privilege,
                section=user_object.section,
				batch=user_object.batch
            )
            
@app.route("/api/<query>", methods=["POST"])
def api_post(query):
    if query == "add_course":
        if not ((session.get("privilege_sess") == 1) or (session.get("privilege_sess") == 2)):
            return "Requires admin/instructor privilege"
            
        add_course_json = request.get_json(force=True)
        # users_object = User.query.filter_by(batch=add_course_json["batch"], section=add_course_json["section"]).all()
        # if users_object is None:
        #     return "No users found"
        course_object = Course.query.filter_by(course_code=add_course_json["course_code"]).first()
        if not course_object is None:
            return "Course code taken"
        
        course = Course(
            course_code=add_course_json["course_code"],
            course_name=add_course_json["course_name"]
        )
        db.session.add(course)
        db.session.commit()
        return "added course"
    else:
        return "Check API query again"

@app.route("/admin/add_course/", methods=["GET"])
def add_course():
    return render_template("addCourse.html")