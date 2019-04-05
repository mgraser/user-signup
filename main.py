from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True   # displays runtime errors in the browser, too

form = """

"""

@app.route("/welcome", methods=['POST'])
def sign_up():
#get and check username and assign error if necessary
     username_arg=request.form["username"]
     password_arg=request.form["pwd"]
     verify_pwd_arg=request.form["verify_pwd"]
     if not username_arg.isalnum() or len(username_arg)<3 or len(username_arg)>20:
         nameerror_arg = "That is not a valid username."
         return render_template("index.html", nameerror=nameerror_arg)
     if not password_arg.isalnum() or len(password_arg)<3 or len(password_arg)>20:
         passworderror_arg = "That is not a valid password."
         return render_template("index.html", pwderror=passworderror_arg)
     if password_arg != verify_pwd_arg:
         verify_pwd_error_arg = "Those passwords don't match."
         return render_template("index.html", verify_pwd_error=verify_pwd_error_arg)
     else:
        return render_template("welcome.html")


#get and check verify pwd and assign error if necessary

#get and check email and assign error if necessary

#if no errors, reirect to welome page

@app.route("/")
def index():
    nameerror = request.args.get("nameerror_arg")
    return render_template("index.html")

app.run()