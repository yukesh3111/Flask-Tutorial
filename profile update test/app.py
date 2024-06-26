from flask import Flask,redirect,render_template,request,url_for,session
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.secret_key="dfsfdfsd;sd[flsfl[pgsd[sdfs'sddsasf55133]]]"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db=SQLAlchemy(app)
class userdetail(db.Model):
    username=db.Column("id",db.String(100),unique=True,primary_key=True)
    password=db.Column("password",db.String(100))
    name=db.Column('name',db.String(100))
    email=db.Column('email',db.String(100))
    phone_no=db.Column('phone',db.Integer())
    def __init__(self,username,password,name,email,phone_no):
        self.username=username
        self.password=password
        self.name=name
        self.email=email
        self.phone_no=phone_no
    def __repr__(self):
        return f"{self.username}:{self.password}:{self.name}:{self.email}:{self.phone_no}"
    
@app.route('/')
def home():
    return render_template("index.html")
@app.route('/signup',methods=['POST','GET'])
def signup():
    if request.method=='POST':
        name=request.form["Name"]
        email=request.form["Email"]
        phone_no=request.form["Phone_no"]
        username=request.form["Username"]
        password=request.form["Password"]
        print(name,email,phone_no,username,password)
        session["User"]=username
        signup_details=userdetail(username=username,password=password,name=name,email=email,phone_no=phone_no)
        db.session.add(signup_details)
        db.session.commit()
        return redirect(url_for("userpro"))
    else:
        if "User" in session:
            return redirect(url_for("userpro"))
        else:    
            return render_template("signup.html")
@app.route('/user-profile')
def userpro():
    user=session["User"]
    userdata=userdetail.query.filter_by(username=user).first()
    print(userdata)
    if("User" in session):  
        return render_template("userprofile.html",username=userdata.username,password=userdata.password,name=userdata.name,email=userdata.email,phone_no=userdata.phone_no)
    else:
        return redirect(url_for("signup"))
@app.route('/logout')
def logout():
    session.pop("user")
    return redirect(url_for("home"))
@app.route('/update-profile',methods=['POST','GET'])
def updatepro():
    user=session["User"]
    if("User" in session and request.method=='POST'):
        
        update=userdetail.query.filter_by(username=user).first()
        print(update)
        update.name=request.form["Name"]
        update.email=request.form["Email"]
        update.phone_no=request.form["Phone_no"]
        db.session.commit()
        return redirect(url_for("userpro"))
    else:
        return render_template("update.html",username=user)

with app.app_context():
    db.create_all()
if(__name__=='__main__'):
    app.run(debug=True)     