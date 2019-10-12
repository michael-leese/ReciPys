#add useful dependencies
import os
from webconfig import MongoDBConfig
from flask import Flask, render_template, redirect, request, url_for
from bson.objectid import ObjectId
from flask_pymongo import PyMongo

app = Flask(__name__)
Config = MongoDBConfig()
#setup Mongo
app.config["MONGO_DBNAME"] = 'myRecipeDB'
app.config["MONGO_URI"] = 'mongodb+srv://root:%s@recipys-giedu.mongodb.net/myRecipeDB?retryWrites=true&w=majority' % (Config.PWconfig)

mongo = PyMongo(app)

@app.route('/')

#retrieve recipy
@app.route('/get_recipys')
def get_recipys():
     return render_template("recipes.html", recipes=mongo.db.recipes.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        # Successfully connected to heroku
