from flask import Blueprint, render_template, Flask, jsonify, request
from flask.views import View
from textblob import TextBlob
from bson import ObjectId  # For ObjectId to work
from pymongo import MongoClient

class HomeView(View):
    def dispatch_request(self):
        return "<h1 style='color:purple'>Hello there !</h1>"

class HelloWorld(View):
    def dispatch_request(self):
        return "<h1 style='color:red'>Hello World !</h1>"

class HelloUser(View):
    def dispatch_request(self, name):
        return "<h1 style='color:red'>" + "Hello {}".format(name) + "!</h1>"

class Person(View):
  def dispatch_request(self, message):
    sentiment = "<h1 style='color:green'>Positive!</h1>"
    if (TextBlob(message).sentiment.polarity < 0.0):
        sentiment = "<h1 style='color:red'>negative!</h1>"
    return f'{sentiment}'

class Username(View):
    def dispatch_request(self, username):
        return f'{username}\'s profile'

class HelloIndex(View):
        #@index_blueprint.route('/hello/<name>/')
    def dispatch_request(self, name):
        return render_template('hello.html', name=name)

class Dbindex(View):
#@index_blueprint.route('/db')
    def dispatch_request(self):
        myclient = MongoClient("mongodb://mongouser:ueb=#r5HHf@localhost:27017/?authSource=admin&authMechanism=SCRAM-SHA-256&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false")
        mydb = myclient["books"]
        mycol = mydb["paperbacks"]

        for x in mycol.find({}, {"_id": 0, "Title": 1, "author": 1}):
            return "<h1 style='color:red'>" + str(x) + "</h1>"
            # print(x)
        myclient.close()

# route to get data from html form and insert data into database
#@index_blueprint.route('/studentsdata', methods=["GET", "POST"])
class StudentData(View):
    def dispatch_request(self):
        # define the mongodb client
        client = MongoClient("mongodb://mongouser:ueb=#r5HHf@localhost:27017/?authSource=admin&authMechanism=SCRAM-SHA-256&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false")
        # define the database to use
        db = client.student_data
        data = {}
        if request.method == "POST":
            data['Name'] = request.form['name']
            data['Email'] = request.form['email']
            data['Age'] = request.form['age']
            data['DOB'] = request.form['dob']
            data['Department'] = request.form['department']
            data['Gender'] = request.form['gender']
            data['Address'] = request.form['address']
            data['Pincode'] = request.form['pincode']
            lang = []
            for i in "1234567":
                try:
                    if request.form['language' + i] != "":
                        lang.append(request.form['language' + i])
                except Exception as e:
                    pass
            data['Language'] = lang
            db.studentData.insert_one(data)
    
        return render_template("students.html")    
        client.close()        