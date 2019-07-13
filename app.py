# import dependencies

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask app

app = Flask(__name__)

@app.route("/")
def index():


@app.route("/scrape")
def scrape():
    mars_data = scrape_mars.scrape_all()

















if __name__ == "__main__":
    app.run()