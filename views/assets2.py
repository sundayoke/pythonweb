from flask import Blueprint, render_template, Flask, jsonify, request
from flask.views import View
from textblob import TextBlob
from bson import ObjectId  # For ObjectId to work
from pymongo import MongoClient
import os
import views.assets

@index_blueprint.route('/with_parameters')
def with_parameters():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    return jsonify(message="My name is " + name + " and I am " + str(age) + " years old")

@index_blueprint.route('/with_url_variables/<string:name>/<int:age>')
def with_url_variables(name: str, age: int):
    return jsonify(message="My name is " + name + " and I am " + str(age) + " years old")
 
# define the Students home page route
@index_blueprint.route('/students')
def hello_world():
    return render_template("students.html")

# define the Blog home page route
@index_blueprint.route('/blog')
def blog_method():
    return "Hello World!"    

