from datetime import datetime
import os
import re
import requests
import sqlite3
import urllib.parse
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from send_mail import send_email, check_ending

app = Flask(__name__)

app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def home():
    # There are two home pages. Registered users will see a list of other users
    if session.get("user_id") is not None:
        profiles = []
        #Go through all the other users from their uni and gather their info
        db = sqlite3.connect("main.db")
        user = session.get("user_id")
        rows = db.execute("SELECT * FROM users WHERE NOT id=? AND university IN (SELECT university FROM users WHERE id=?) AND id NOT IN (SELECT blockee FROM blocked WHERE blocker=?) AND id NOT IN (SELECT blocker FROM blocked WHERE blockee=?) ORDER BY university, firstName", (user,user, user, user,)).fetchall()
        db.close()
        for row in rows:
            row = list(row)
            #If they have a bio, include it.
            if row[7] is not None:
                bio = row[7]
            else:
                bio = ""
            #If they have a picture, select the most recent one. Otherwise, use the default
            if row[8] == 0:
                picUrl = "/static/user-icon.png"
            else:
                picList = os.listdir("./static/profile-pics/" + str(row[0]))
                time = 0
                picUrl = "/static/user-icon.png"
                for currPic in picList:
                    filePath = os.path.join("./static/profile-pics/" + str(row[0]), currPic)
                    if os.path.getmtime(filePath) > time:
                        time = os.path.getmtime(filePath)
                        picUrl = filePath
            profiles.append({"name":str(row[5]).title(),"email":row[3],"id":row[0],"university":row[6],"bio":bio,"picUrl":picUrl})
        return render_template("index.html", profiles=profiles)
    return render_template("landing.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        db = sqlite3.connect("main.db")
        # Ensure email was submitted
        if not request.form.get("email"):
            return render_template("loginFailed.html", error="Please enter your email")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return render_template("loginFailed.html", error="Please enter a password")

        # Query database for email
        rows = db.execute("SELECT * FROM users WHERE email = ?", (request.form.get("email"),)).fetchall()

        # Ensure email exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0][2], request.form.get("password")):
            return render_template("loginFailed.html", error="Incorrect email or password")

        # Remember which user has logged in
        session["user_id"] = rows[0][0]
        if rows[0][4] == 0:
            session["verified"] = False
        else:
            session["verified"] = True

        db.close()

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    # Forget any user_id
    session.clear()

    # Redirect user to home page
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    session.clear()

    """Register user"""
    #If the request method is get, render a form to allow them to input info
    #The form should post that info back to /register
    if request.method == "GET":
        return render_template("register.html")

    #Validate the response server-side before storing at as a new user in finance.db
    if request.method=="POST":
        db = sqlite3.connect("main.db")
        #Make sure first name and university are entered
        if not request.form.get("firstName"):
            return render_template("registrationFailed.html", error="Please enter your first name.")
        if not request.form.get("university") or request.form.get("university") == "University":
            return render_template("registrationFailed.html", error="Please select a university.")

        #Do the same for email, but use regex to make sure it is a valid email ending in .edu
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

        if not request.form.get("email") or not re.fullmatch(regex, request.form.get("email")) or not check_ending(request.form.get("email"), ".edu"):
            return render_template("registrationFailed.html", error="Please enter a valid email address ending in .edu")
        for row in db.execute("SELECT * FROM users WHERE email = ?", (request.form.get("email"),)):
            return render_template("registrationFailed.html", error="Email already in use.")
        #Make sure neither password is blank
        if not request.form.get("password"):
            return render_template("registrationFailed.html", error="Please enter a password.")
        if not request.form.get("confirmation"):
            return render_template("registrationFailed.html", error="Must confirm password.")

        #Make sure the passwords match
        if request.form.get("password") != request.form.get("confirmation"):
            return render_template("registrationFailed.html", error="Password and confirmation must match.")

        #Disallow forbidden characters in password
        forbiddenChars = [",",";","'","\"",":"]
        for char in forbiddenChars:
            if char in request.form.get("password"):
                return render_template("registrationFailed.html", error="Password must not contain any of the following characters: , ; ' \" :")

        #Store the new user
        username = "Null"
        hash = generate_password_hash(request.form.get("password"), method='pbkdf2:sha256', salt_length=8)
        email = request.form.get("email")
        db.execute("INSERT INTO users (username, hash, email, firstName, university) VALUES(?, ?, ?, ?, ?)", (username, hash, email, request.form.get("firstName"), request.form.get("university")))
        db.commit()
        db.close()
        
        #Send a registration success email
        #TODO Uncomment this function!
        send_email(email, "Registration success!", "Good job!")

        #After storing the new user, render registered template which extends /login with a success message
        return render_template("registered.html")

#Allow the user to see and edit their profile
@app.route("/profile", methods=["GET", "POST"])
def profile():
    if request.method == "POST":
        #Check and handle a file
        if 'picSelect' in request.files and len(request.files['picSelect'].filename) > 0:
            f = request.files['picSelect']
            dir = "C:\\Users\\aubre\\Documents\\OwlHacks\\gymBuddies\\static\\profile-pics\\" + str(session.get("user_id"))
            if not os.path.exists(dir):
                os.mkdir(dir)
            f.save(os.path.join(dir , secure_filename(f.filename)))
            db = sqlite3.connect("main.db")
            db.execute("UPDATE users SET pic = 1 WHERE id = ?", (session.get("user_id"),))
            db.commit()
            db.close()
        #Handle the bio
        bio = request.form.get("bio")
        if bio != "This person's bio is empty.":
            db = sqlite3.connect("main.db")
            db.execute("UPDATE users SET bio = ? WHERE id = ?", (bio,session.get("user_id"),))
            db.commit()
            db.close()
        return redirect("/profile")
    if session.get("user_id") is None:
        return redirect("/")
    db = sqlite3.connect("main.db")
    rows = db.execute("SELECT * FROM users WHERE id=?", (session.get("user_id"),)).fetchall()
    db.close()
    id = rows[0][0]
    email = rows[0][3]
    verified = (rows[0][4] != 0)
    firstName = rows[0][5]
    uni = rows[0][6]
    bio = rows[0][7]
    if bio is None:
        bio = "This person's bio is empty."
    pic = (rows[0][8] != 0)
    picUrl = "/static/user-icon.png"
    if pic:
        picList = os.listdir("./static/profile-pics/" + str(session.get("user_id")))
        time = 0
        for currPic in picList:
            filePath = os.path.join("./static/profile-pics/" + str(session.get("user_id")), currPic)
            if os.path.getmtime(filePath) > time:
                time = os.path.getmtime(filePath)
                picUrl = filePath
    return render_template("profile.html",id=id,username="Null",email=email,verified=verified,
                            firstName=firstName,uni=uni,bio=bio,pic=pic, picUrl=picUrl)

@app.route("/message", methods=["GET","POST"])
def message():
    #If reached via get, ensure that they have a user selected and then allow them to message that user
    if request.method == "GET":
        if "u" not in request.args.keys():
            return render_template("403.html")
        id = request.args.get("u")
        db = sqlite3.connect("main.db")
        rows = db.execute("SELECT * FROM blocked WHERE (blockee=? AND blocker=?) OR (blocker=? AND blockee=?)", (session.get("user_id"),id,session.get("user_id"), id))
        for row in rows:
            return render_template("403.html")
        rows = db.execute("SELECT firstName FROM users WHERE id=? LIMIT 1", (id,))
        for row in rows:
            name = row[0]
        db.close()
        return render_template("message.html", id=id, name=name)
    #If reached via post, update the database to save the messages
    else:
        if not request.form.get("id") or not request.form.get("message"):
            return redirect("/")
        db = sqlite3.connect("main.db")
        #User 1 is from while user 2 is to
        db.execute("INSERT INTO messages (body, user1, user2, time) VALUES (?, ?, ?, ?)", (request.form.get("message"),session.get("user_id"), request.form.get("id"), datetime.now()))
        db.commit()
        db.close()
        return redirect("/")
        
@app.route("/inbox", methods=["GET"])
def inbox():
    db = sqlite3.connect("main.db")
    inbox = []
    #Go through all messages and create a card for each
    #The from flag allows users to filter by sender
    if "from" in request.args.keys():
        messages = db.execute("SELECT user1,body FROM messages WHERE user2=? AND user1=? ORDER BY time DESC", (session.get("user_id"),request.args.get("from")))
    else:
        messages = db.execute("SELECT user1,body FROM messages WHERE user2=? ORDER BY time DESC", (session.get("user_id"),))
    for message in messages:
        #Get each sender, and cleanup the input
        names = db.execute("SELECT firstName FROM users WHERE id=? LIMIT 1", (message[0],))
        for currName in names:
            currName = list(currName)
            name = currName[0]
        inbox.append({"name":name,"text":message[1],"id":message[0]})
    db.close()
    return render_template("inbox.html", inbox=inbox)

@app.route("/sent", methods=["GET"])
def sent():
    db = sqlite3.connect("main.db")
    sent = []
    #Go through all messages and create a card for each
    #The to flag allows users to filter by recipient
    if "to" in request.args.keys():
        messages = db.execute("SELECT user2,body FROM messages WHERE user1=? AND user2=? ORDER BY time DESC", (session.get("user_id"),request.args.get("to")))
    else:
        messages = db.execute("SELECT user2,body FROM messages WHERE user1=? ORDER BY time DESC", (session.get("user_id"),))
    for message in messages:
        #Get each recipient, and cleanup the input
        names = db.execute("SELECT firstName FROM users WHERE id=? LIMIT 1", (message[0],))
        for currName in names:
            currName = list(currName)
            name = currName[0]
        sent.append({"name":name,"text":message[1],"id":message[0]})
    db.close()
    return render_template("sent.html", sent=sent)

@app.route("/block", methods=["GET"])
def block():
    if "u" not in request.args.keys():
        return redirect("/")
    db = sqlite3.connect("main.db")
    db.execute("INSERT INTO blocked (blocker, blockee) VALUES(?, ?)", (session.get("user_id"), request.args.get("u"),))
    db.commit()
    db.close()
    return redirect("/")
