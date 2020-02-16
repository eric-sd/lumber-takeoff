import os
from flask import Flask, render_template, request
from takeoff import convertToInches, figureOutStuds
app = Flask(__name__)

@app.route('/')
def lumber():
   return render_template('lumber.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      totalStuds = figureOutStuds(result['width'],result['studSpacing'])
      newResult = {'Wall Width' : result['width'], 'Stud Spacing' : result['studSpacing'], 'Total Studs' : totalStuds}
      return render_template("result.html",result = newResult)

port = int(os.environ.get("PORT", 5000))
app.run(debug=True,host='0.0.0.0',port=port)

