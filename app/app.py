# import dependencies

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask app

app = Flask(__name__)

# Use PyMongo to establish Mongo connection

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def index():


# @app.route("/scrape")
# def scrape():
#     mars_data = scrape_mars.scrape_all()

















if __name__ == "__main__":
    app.run()