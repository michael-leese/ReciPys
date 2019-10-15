#add useful dependencies
import os
import re
import bcrypt
from webconfig import MongoDBConfig
from flask import Flask, render_template, redirect, request, url_for
from bson.objectid import ObjectId
from flask_pymongo import PyMongo
from forms import Add_Recipe, Registration

app = Flask(__name__)

Config = MongoDBConfig()
#setup Mongo
app.config["MONGO_DBNAME"] = 'myRecipeDB'
app.config["MONGO_URI"] = Config.PWconfig

mongo = PyMongo(app)

@app.route('/')

#retrieve home page and return top 4 viewed recipes
@app.route('/index')
def index():
    most_viewed = mongo.db.recipes.find().sort([('views', -1)]).limit(4)
    return render_template("index.html", title="Home", recipes=most_viewed)

#registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = Registration(request.form, csrf_enabled=False)
    if form.validate_on_submit():
        # get all the users
        users = mongo.db.users
        # see if we already have the entered username
        user_name = request.form['username']
    #using regular expression setting option for any case
        user_check = {'$regex': re.compile('\W*({})\W*'.format(user_name)), '$options': 'i'}
        user_check = users.find_one({'username': request.form['username']})
        if user_check is None:
            # hash the entered password
            password = request.form['password'].encode('utf-8')
            hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
            # insert the user to DB
            users.insert_one({'username': request.form['username'],
                          'password': hashed_password,
                          'firstname': request.form['firstname'],
                          'lastname': request.form['lastname'],
                          'email': request.form['email'],
                          'dob': request.form['dob']})
            return redirect(url_for('index'))
        error_message = "That Username is already taken. Please try again."
        return render_template("error.html", title="ERROR", error=error_message, last_page='../register')
    return render_template("register.html", form=form, title="Register")

#retrieve user page
@app.route('/my_recipys')
def my_recipys():
    return render_template("myrecipys.html", users=mongo.db.users.find(), title="User")

#retrieve recipy page
@app.route('/recipys')
def recipys():
    return render_template("recipys.html", recipes=mongo.db.recipes.find(), title="Larder")

#add recipy page
@app.route('/add_recipy', methods=['GET', 'POST'])
def add_recipy():
    form = Add_Recipe(request.form, csrf_enabled=False)
    if form.validate_on_submit():
        # set the collection
        recipes_db = mongo.db.recipes
        # add new recipe
        recipes_db.insert_one({
            'creator': request.form['creator'],
            'title': request.form['title'],
            'description': request.form['description'],
            'ingredients': request.form['ingredients'],
            'instructions': request.form['instructions'],
            'tags': request.form['tags'],
            'imageLink': request.form['imageLink'],
            'views': '1'
            })
        return redirect(url_for('index', title='SAVED!'))
    return render_template('add_recipy.html', form=form, title='Add ReciPy')

#search for recipes from home screen
@app.route('/search_recipes')
def search_recipes():
    #get value from the search box
    chosenRecipe = request.args['chosenWord']
    #using regular expression setting option for any case
    searchInput = {'$regex': re.compile('.*{}.*'.format(chosenRecipe)), '$options': 'i'}
    #search recipes in DB for the word in title, tags or ingredients
    results = mongo.db.recipes.find({
        '$or': [
            {'title': searchInput},
            {'tags': searchInput},
            {'ingredients': searchInput},
        ]
    })
    return render_template('searchresults.html', query=chosenRecipe, results=results, title="Results")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        # Successfully connected to heroku
