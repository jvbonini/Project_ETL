from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import pandas as pd
import NCAA_data
import os

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
# app.config["MONGO_URI"] = "mongodb://localhost:27017/NCAA_app"
# mongo = PyMongo(app)

app.config["MONGO_URI"] = os.environ.get('authentication')
mongo = PyMongo(app)


# connect to mongo db and collection
# db = client.NCAA_data
# collection = db.produce

@app.route("/")
def index():
    NCAA_info = mongo.db.collection.find()
    print(NCAA_info)
    return "This is our homework that has been rendered through Flask"
    return render_template("index.html", NCAA_info = NCAA_info)


@app.route("/NCAA player data")
def scraper():
    NCAA_info = mongo.db.NCAA_info
    player_data = NCAA_data.player_stats()
    NCAA_info.update({}, player_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)



