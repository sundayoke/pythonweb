from flask import Flask
from textblob import TextBlob
from controllers.index import index_blueprint
from bson import ObjectId # For ObjectId to work    
from pymongo import MongoClient    
import os  

app = Flask(__name__)

app.register_blueprint(index_blueprint)
## Uncomment line nelow to run from local host
#if __name__ == "__main__": app.run(host='0.0.0.0')
