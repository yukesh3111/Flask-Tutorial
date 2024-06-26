from flask import Flask,redirect,url_for
app=Flask(__name__)
@app.route('/')
def home():
    return "<h2>Hello world</h2>"
@app.route('/<name>')
def url(name):
    return f"Hello {name}"
@app.route('/admin')
def admin():
    return redirect(url_for("home"))
if __name__=="__main__":
    app.run()