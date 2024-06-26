from flask import Flask,render_template
app=Flask(__name__)
#@app.route('/')
#def home():
#    return render_template('home.html') 
@app.route('/')
def index():
    list1=['yukesh','vasanth','partha']
    return render_template('home.html',content=list1,num=3) 
if __name__=='__main__':
    
    app.run(debug=True)