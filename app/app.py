import os
from flask import Flask, render_template, request
from takeOff import convertToInches, figureOutStuds
import configparser

config = configparser.ConfigParser()
config.read("takeOff.ini")


version = config["metadata"]["version"]

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def lumber():
   return render_template('lumber.html', version = version)

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      totalStuds = 0
      newResult = {}
      newResult['Stud Spacing'] = str(result['studSpacing']) + " inches "
      for fieldname, value in result.items():
          if value:
              if 'width' in fieldname.casefold() and int(value) > 0:
                  totalStuds = totalStuds + figureOutStuds(result[fieldname],result['studSpacing'])
                  newResult[fieldname] = str(value) + " feet"

      newResult['Total Studs Needed'] = totalStuds
      return render_template("result.html",result = newResult)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0',port=port)

