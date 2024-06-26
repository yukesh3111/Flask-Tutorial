from flask import Flask,request,flash,redirect,render_template,url_for,session
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.secret_key="sdjkfjoeihoISHDFODOfhoisehoSIOFhasF;oeefhe[p[pojfa]]asd"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db=SQLAlchemy(app)

class user(db.Model):
    _id=db.Column("id",db.Integer,primary_key=True)
    email=db.Column ("email",db.String(50),unique=True)
    password=db.Column("password",db.String(50))
    def __init__(self,email,password):
        self.email=email
        self.password=password
    def __repr__(self):
        return f"{self.email}:{self.password}"
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/login',methods=['POST','GET'])
def login():
    if(request.method=='POST'):
        email=request.form["Email"]
        password=request.form["Password"]
        session["email"]=email
        session["password"]=password
        athenti=user(email=email,password=password)
        db.session.add(athenti)
        db.session.commit()
        print(athenti)
        flash("log in Successfully!!")
        return redirect(url_for('userpro'))
    else:
        if "email" and "password" in session:
            flash("You already logged in")
            return redirect(url_for("userpro"))
        return render_template("login.html")
@app.route('/user')
def userpro():
    if "email" and "password" in session:
        athenticate=user.query.all()
        print(athenticate)
        return render_template("userprofile.html",authicate=athenticate)
    else:
        return redirect(url_for("login"))
@app.route('/update',methods=['POST','GET'])
def update():
    if request.method=='POST':
        cha_email=request.form["Email"]
        new_password=request.form["new-Password"]
        update=user.query.filter_by(email=cha_email).first()
        update.password=new_password
        db.session.commit()
        flash(f"Updated Sucessfully!!")
        return redirect(url_for("userpro"))
    else:
        return render_template("update.html")
@app.route('/logout')
def logout():
    session.pop("email")
    session.pop("password")
    flash("log out Successfully!!")
    return redirect(url_for("login"))

with app.app_context():
    db.create_all()

if __name__=="__main__":
    app.run(debug=True)