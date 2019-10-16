#add useful dependencies
import os
import re
import bcrypt
from webconfig import MongoDBConfig, Keys
from flask import Flask, render_template, redirect, request, url_for, session
from bson.objectid import ObjectId
from flask_pymongo import PyMongo
from forms import Add_Recipe, Registration, Login

app = Flask(__name__)

Config = MongoDBConfig()
Keys =Keys()
#setup Mongo
app.config["MONGO_DBNAME"] = 'myRecipeDB'
app.config["MONGO_URI"] = Config.PWconfig
app.config['SECRET_KEY'] = Keys.SECRET_KEY

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
            #set up a session for the new user
            session['username'] = user_name
            session['logged_in'] = True
            return redirect(url_for('welcome_user'))
        error_message = "That Username is already taken. Please try again."
        return render_template("error.html", title="ERROR", error=error_message, last_page='../register')
    return render_template("register.html", form=form, title="Register")

#retrieve welcome_user page for first timers
@app.route('/welcome_user')
def welcome_user():
    #pick the username up from the session they have
    user = session['username']
    return render_template("first_login_page.html", title="Welcome", user=user)

#retrieve login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    #
    if session.get('logged_in'):
        if session['logged_in'] is True:
            return redirect(url_for('index', title="Signed In"))

    form = Login(request.form, csrf_enabled=False)

    if form.validate_on_submit():
        # get all users
        users = mongo.db.users
        # try and get one with same name as entered
        db_user = users.find_one({'username': request.form['username']})
        
        if db_user:
            #set up the salt_password
            salt_password = request.form['password'].encode('utf-8')
            #get the value of input password
            input_password = bcrypt.hashpw(salt_password, db_user['password'])
            # check password using hashing
            if input_password == db_user['password']:
                session['username'] = request.form['username']
                session['logged_in'] = True
                # successful redirect to home logged in
                return redirect(url_for('index', title="Signed In", form=form))
            error_message = "Username/Password Incorrect!"
            return render_template("error.html", title="ERROR", error=error_message, last_page='../login')
    return render_template("login.html", title="Login", form=form)

#logout the user and return to home page
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

#retrieve user page
@app.route('/my_recipys')
def my_recipys():
    # get all recipes
    recipes = mongo.db.recipes
    #get logged in username
    user = session['username']
    #using regular expression setting option for any case
    creator = {'$regex': re.compile('\W*({})\W*'.format(user)), '$options': 'i'}
    #find there recipys on db
    my_recipys = recipes.find({'$or': [{'creator': creator}]})
    return render_template("myrecipys.html", my_recipys=my_recipys, title="User")

#retrieve recipy page
@app.route('/recipys')
def recipys():
    #get all recipes
    return render_template("recipys.html", recipes=mongo.db.recipes.find(), title="Larder")

#get one recipe
@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):
   
    recipe_id = recipe_id

    # get all recipes
    recipes = mongo.db.recipes
    
    recipes.find_one_and_update(
        {'_id': ObjectId(recipe_id)},
        {'$inc': {'views': 1}}
    )
    recipe = recipes.find_one({'_id': ObjectId(recipe_id)})
    return render_template("recipe.html", recipe=recipe, title="ReciPy")

#add recipy page
@app.route('/add_recipy', methods=['GET', 'POST'])
def add_recipy():
    form = Add_Recipe(request.form, csrf_enabled=False)
    if form.validate_on_submit():
        # set the collection
        recipes_db = mongo.db.recipes
        # add new recipe
        recipes_db.insert_one({
            'creator': session['username'],
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
