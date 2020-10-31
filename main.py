# importing libraries
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from detect import detect
import os

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route("/result" ,methods = ["GET", "POST"])
def result():
  if request.method == 'POST':
    f = request.files.get('file')
    f.save(os.path.join("/home/dhruv/app/static/output/", secure_filename(f.filename)))
    filepath = os.path.join("/home/dhruv/app/static/output/", secure_filename(f.filename))
    result = detect(source=filepath, weights=['static/Weights/best.pt'], conf_thres=0.4)
    st = "Your Predicted result is "
    result = st + str(result)
    print(result)
    return render_template("result.html", result=result, newimage=f.filename)
  return render_template("index.html")


if __name__ == "__main__":
  app.run(host = "0.0.0.0", port = 12000, debug = True)