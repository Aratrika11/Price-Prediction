from flask import Flask,request,jsonify
from flask_cors import CORS
import util

app= Flask(__name__)

@app.route('/get_location')
def get_location():
  response = jsonify({
    'Region': util.get_location()
  })
  response.headers.add('Access-Control-Allow-Origin','*')

  return response

@app.route('/predict_homeprc',methods=['GET','POST'])
def predict_homeprc():
  Total_Sqft = float(request.form['Total_Sqft'])
  Region = request.form['Region']
  BHK = int(request.form['BHK'])
  EMI_Starts = float(request.form['EMI_Starts'])

  response = jsonify({
    'estimated_price': util.get_price_estimate(Region,Total_Sqft,BHK,EMI_Starts)
  })

  response.headers.add('Access-Control-Allow-Origin','*')
  Access-Control-Allow-Methods: GET, POST, PUT, DELETE
  Access-Control-Allow-Headers: Content-Type, Authorization
  Access-Control-Allow-Credentials: true

  return response

CORS(app, origins=["http://127.0.0.1:5000/predicted_homeprc"], methods=["GET", "POST"], allow_headers=["Content-Type", "Authorization"])


  '''@app.route('/predict_homeprc', methods=['GET', 'POST'])
def predict_homeprc():
    total_sqft = float(request.form['Total_Sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    emi = int(request.form['EMI'])

    response = jsonify({
        'estimated_price': util.get_price_estimate(location,total_sqft,bhk,emi)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response'''

if __name__=='__main__':
  print("Starting Python Flask Server For House Price Prediction")
  util.load_saved_artifacts()
  app.run()
