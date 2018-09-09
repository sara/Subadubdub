from flask import Flask,render_template, request, redirect, url_for, make_response, jsonify
from threading import Thread
import sys
sys.path.append("..")
import workflow as wf
import os
from pathlib import Path
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")
@app.route("/workflow",methods=['POST','GET'])
def workflow():
    #mp4input = "parksandrec.mp4"
   # script = "script.txt"
  #  lang_ = "de"
 #   thread = Thread(target = wf.begin_workflow,args = [script,mp4input,lang_]) 
#    thread.start()
    print("render template?")
    return render_template("display.html")
    
@app.route("/poll")
def poll():
    my_file = Path("results/final.mp4")
    if not my_file.exists():
        resp = {"resp":"Nah"}
        return jsonify(resp)
    else:
        resp = {"resp":"Yeet"}
        return jsonify(resp)
    
@app.route('/display')
def display():
    return render_template("display.html")
    


if __name__ == '__main__':
    app.run(debug = True)
