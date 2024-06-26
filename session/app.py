from flask import Flask,session,render_template,redirect,request,url_for
app=Flask(__name__)
app.secret_key="yuias1234jasd923rofshkebndmgjefkjlg89r238r923hwefj[];whjij"
@app.route('/')
def home():
    return render_template("index.html")
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        user=request.form["username"]
        session["user"]=user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        else:
            return render_template("login.html")
@app.route('/user')
def user():
    if("user" in session):
        user=session["user"]
        return f"<h2>{user}</h2>"
    else:
        return redirect(url_for('login'))
@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect(url_for("login"))
if __name__=='__main__':
    app.run(debug=True)