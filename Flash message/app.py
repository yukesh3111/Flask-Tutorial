from flask import Flask,render_template,request,url_for,redirect,session,flash
app=Flask(__name__)
app.secret_key="sdadasnmnasdnioqwl1234213,m./,m/f/klenffs.dbfniul[ddfjod[]]"
@app.route('/')
def home():
    return render_template("index.html")
@app.route('/login',methods=["POST","GET"])
def login():
    if(request.method=='POST'):
        user=request.form["username"]
        session["user"]=user
        flash(f"Hey Login successfully")
        return redirect(url_for("userpro"))
    else:
        if "user" in session:
            flash(f"Hey user already login")
            return redirect(url_for("userpro"))
        else:
            return render_template("login.html")
@app.route('/user')
def userpro():
    if "user" in session:
        user=session["user"]
        return render_template("userprofile.html",user=user)
    else:
        return redirect(url_for("login"))
@app.route('/logout')
def logout():
    flash(f"Logout Successfully!")
    session.pop("user",None)
    return redirect(url_for("login"))
        
if __name__=="__main__":
    app.run(debug=True)
