from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

#cd /var/www/html/peakstream.net/public_html/pythonweb
#python -m venv /var/www/html/peakstream.net/public_html/pythonweb/env
#source ./env/bin/activate
#python -m flask run
#uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi:app