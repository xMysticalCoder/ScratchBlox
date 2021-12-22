from flask import Flask, redirect, url_for, render_template, request, jsonify
from replit import db
#format is below
#db[username] = [password,score1, score2, score3]
#to access game 1 score, do db[username][1]

app = Flask(__name__)

@app.route("/home")
def home1():
  return render_template("home.html")
@app.route("/")
def home():
  return render_template("home.html")

@app.route("/signup")
def signup():
  return render_template("signup.html")

@app.route("/login")
def login():
  return render_template("login.html")
@app.route("/signedup", methods=["GET", "POST"])
def signedup():
  if request.method == "POST":
    username = request.form.get("username")
    password = request.form.get("password")
    gl = [password]
    if username in db.keys() or username.lower() == "games":
      return render_template("usernameTaken.html")
    else:
      for i in range(int(db["games"])):
        gl = gl + [""]

      db[username] = gl
      return redirect(url_for("homepage"))
@app.route("/loggedin", methods=["GET", "POST"])
def loggedin():
  if request.method == "POST":
    username = request.form.get("usernamelogin")
    password = request.form.get("passwordlogin")
    if username in db.keys():
      if db[username][0] == password:
        return redirect(url_for("homepage"))
      else:
        return render_template("credintialsInvalid.html")
    else:
      return render_template("credintialsInvalid.html")
    
@app.route("/users")
def users():

  return f"<body bgcolor = orange>{str(db.keys())}</body>"

@app.route("/homepage", methods=["GET", "POST"])
def homepage():
  if request.form.get("usernamelogin") or request.form.get("username") != None:
    return redirect(url_for("login"))
  else:
    return f"Welcome {username}!"
    
 
    
  
if __name__ == "__main__":
  app.run("0.0.0.0")