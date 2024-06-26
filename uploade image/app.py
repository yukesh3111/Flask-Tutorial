import os
import cv2
from flask import Flask,request,render_template,redirect,url_for
from ultralytics import YOLO
from werkzeug.utils import secure_filename
from ultralytics import YOLO
import re

UPLOAD_FOLDER = r'uploade image\static\uploadeimage'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def predict (image_path):
    infer=YOLO(r"best.pt")
    result=infer.predict(image_path,save=True,save_txt=True)
    total_trees = 0

    for result in result:
        total_trees += len(result.boxes)

    print("Total number of trees detected:", total_trees)


@app.route('/',methods=["GET","POST"])
def upload():
    if request.method=="POST":
        file=request.files["image"]
        filename=secure_filename(file.filename)
        print(filename)
        image_path=filename
        file.save(image_path)
        predict(image_path)
        return render_template("index.html")
    else:
        return render_template("index.html")    
if(__name__=="__main__"):
    app.run(debug=True)
