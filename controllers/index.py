from flask import Blueprint, render_template, Flask, jsonify, request
from flask.views import View
from textblob import TextBlob
from bson import ObjectId  # For ObjectId to work
from pymongo import MongoClient
import os
import views.assets



index_blueprint = Blueprint('index', __name__)

index_blueprint.add_url_rule('/pythonweb', view_func=views.assets.HomeView().as_view('home_view'))
index_blueprint.add_url_rule('/pythonweb/yo', view_func=views.assets.HelloWorld.as_view('hello_world'))
index_blueprint.add_url_rule('/pythonweb/yo/<string:name>', view_func=views.assets.HelloUser.as_view('hello_user'))
index_blueprint.add_url_rule('/pythonweb/message/<string:message>', view_func=views.assets.Person.as_view('person'))
index_blueprint.add_url_rule('/pythonweb/user/<string:username>', view_func=views.assets.Username.as_view('username'))
index_blueprint.add_url_rule('/pythonweb/hello/<string:name>', view_func=views.assets.HelloIndex.as_view('hello_index'))
index_blueprint.add_url_rule('/pythonweb/db', view_func=views.assets.Dbindex.as_view('dbindex'))
index_blueprint.add_url_rule('/pythonweb/studentsdata', view_func=views.assets.StudentData.as_view('studentdata'))


