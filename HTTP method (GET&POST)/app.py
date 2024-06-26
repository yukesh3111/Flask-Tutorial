from flask import Flask,render_template,url_for,redirect,request
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/login',methods=['GET','POST'])
def login():
    if(request.method=='POST'):
        user=request.form["username"]
        return redirect(url_for("user",usr=user))
    else:
        return render_template("login.html")
@app.route('/<usr>')
def user(usr):
    if(usr=="yukesh"):
        return f"<h2>{usr} Login succesfully</h2>"
    else:
        return f"<h2>{usr} invalid login</h2>"
if __name__=='__main__':
    app.run(debug=True) 
