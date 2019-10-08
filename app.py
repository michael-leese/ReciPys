#add useful dependencies
import os
from webconfig import MongoDBConfig
from flask import Flask, render_template, redirect, request, url_for
from bson.objectid import ObjectId
from flask_pymongo import PyMongo

app = Flask(__name__)

#setup Mongo
app.config["MONGO_DBNAME"] = 'myRecipeDB'
app.config["MONGO_URI"] = 'mongodb+srv://root:%s@recipys-giedu.mongodb.net/myRecipeDB?retryWrites=true&w=majority' % (MongoDBConfig.PWconfig)

mongo = PyMongo(app)

#Setup simple message to show server setup is working
@app.route('/')
@app.route('/get_users')
def get_users():
    return render_template("index.html", users=mongo.db.users.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        # Successfully connected to heroku
