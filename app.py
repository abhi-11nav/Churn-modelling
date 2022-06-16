#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 14:40:11 2022

@author: abhinav
"""
from flask import Flask, render_template, request
import numpy
import pickle


app = Flask(__name__,template_folder="template")

classifier = pickle.load(open("classifier.pkl","rb"))

@app.route("/",methods=["GET"])
def home():
    return render_template("/index.html")

@app.route("/",methods=["POST"])
def predict():
    if request.method == "POST":
        
        Credit_score = request.form['credit_score']
        
        Geography = request.form['geography']
        if (Geography=="france"):
            Geography=0
        elif (Geography=="spain"):
            Geogrpahy=2
        else:
            Geogrpahy=1
            
        Gender = request.form["gender"]
        if (Gender=="male"):
            Gender = 1
        else:
            Gender = 0  
            
        Age = request.form['age']
            
        Tenure = request.form["tenure"]
        
        Balance = request.form["balance"]
        
        Number_of_products = request.form["no_of_prodcuts"]
        
        Credit_card = request.form["credit_card"]
        if(Credit_card == "yes"):
            Credit_card = 1
        else:
            Credit_card = 0
            
        Active_member = request.form['active_member']
        if(Active_member == "yes"):
            Active_member = 1
        else:
            Active_member = 0
            
        Estimated_Salary = request.form["estimated_salary"]
        
        features = np.array([Credit_score, Geography, Gender, Age, Tenure, Balance, Number_of_products, Credit_card, Active_member, EstimatedSalary])
    
        features = features.reshape(1,-1)
        
        prediction = classifier.predict(features)
        
        
        if(prediction == 1):
            return render_template("/index.html", prediction_text = "THE CUSTOMER HAS EXITED THE BANK ")
        else:
            return render_template("/index.html", prediction_text = "THE CUSTOMER HAS NOT EXITED THE BANK ")
        
if __name__ == "__main__":
    app.run(debug=True)
 