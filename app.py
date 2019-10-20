#add useful dependencies
import os
import re
import bcrypt
from webconfig import MongoDBConfig, Keys
from flask import Flask, render_template, redirect, request, url_for, session
from bson.objectid import ObjectId
from flask_pymongo import PyMongo
from forms import Add_Recipe, Registration, Login, Edit_Recipe

app = Flask(__name__)
#get web.config settings
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
    #see if a user logged in 
    if 'username' in session:
        session['logged_in'] = True
        #search the database for top 4 recipys
        most_viewed = mongo.db.recipes.find().sort([('views', -1)]).limit(4)
        #go to the home page with logged in true
        return render_template("index.html", title="Home", recipes=most_viewed)
    #go to the home page
    most_viewed = mongo.db.recipes.find().sort([('views', -1)]).limit(4)
    return render_template("index.html", title="Home", recipes=most_viewed)

#registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    #get form
    form = Registration(request.form, csrf_enabled=False)
    #if register button  is pressed
    if form.validate_on_submit():
        # get all the users from the database
        users = mongo.db.users
        # see if we already have the entered username
        user_name = request.form['username']
        #using regular expression get exact match
        user_check = {'$regex': re.compile('\W*({})\W*'.format(user_name)), '$options': 'i'}
        #find one in database
        user_check = users.find_one({'username': request.form['username']})
        #if user not in the database
        if user_check is None:
            # hash the entered password
            password = request.form['password'].encode('utf-8')
            #compare password to password in database
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
            #go to welcome user page for first time logged in page
            return redirect(url_for('welcome_user'))
        error_message = "That Username is already taken. Please try again."
        #user exists go to error page with message
        return render_template("error.html", title="ERROR", error=error_message, last_page='../register')
    #go to the blank registration form
    return render_template("register.html", form=form, title="Register")

#retrieve welcome_user page for first timers
@app.route('/welcome_user')
def welcome_user():
    #pick the username up from the session they have
    user = session['username']
    #got to the welcome to recipys first page.
    return render_template("first_login_page.html", title="Welcome", user=user)

#retrieve login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    #check to see is user is logged in
    if session.get('logged_in'):
        if session['logged_in'] is True:
            #send to index signed in
            return redirect(url_for('index', title="Signed In"))
    #get the form
    form = Login(request.form, csrf_enabled=False)
    #if login button is pressed
    if form.validate_on_submit():
        # get all users
        users = mongo.db.users
        # try and get one with same name as entered
        db_user = users.find_one({'username': request.form['username']})  
        #if user in database
        if db_user:
            #set up the salt_password for decryption
            salt_password = request.form['password'].encode('utf-8')
            #get the value of input password
            input_password = bcrypt.hashpw(salt_password, db_user['password'])
            # check password matches using hashing
            if input_password == db_user['password']:
                #if logged in user same as user in database
                session['username'] = request.form['username']
                session['logged_in'] = True
                #go to home page logged in
                return redirect(url_for('index', title="Signed In", form=form))
            error_message = "Username/Password Incorrect!"
            #go to the error page
            return render_template("error.html", title="ERROR", error=error_message, last_page='../login')
    #go to the log in page
    return render_template("login.html", title="Login", form=form)

#logout the user and return to home page
@app.route('/logout')
def logout():
    #clear users session and logout
    session.clear()#go back to home logged out
    return redirect(url_for('index'))

#retrieve user page
@app.route('/my_recipys')
def my_recipys():
    #get last page url from request
    last_page = request.referrer
    # get all recipes
    if 'username' in session:
        #get the recipes from database
        recipes = mongo.db.recipes
        #get logged in username
        user = session['username']
        #using regular expression to search for exact expresions
        creator = {'$regex': re.compile('\W*({})\W*'.format(user)), '$options': 'i'}
        #find there recipys on database
        my_recipys = recipes.find({'$or': [{'creator': creator}]})
        #got to logged in user page with all users recipes
        return render_template("myrecipys.html", my_recipys=my_recipys, last_page=last_page, title="Cookopedia")
    #go to unlogged in myrecipys page here pointing to registration
    return render_template("myrecipys.html", last_page=last_page, title="Cookopedia")

#retrieve recipy page
@app.route('/recipys')
def recipys():
    #get all recipes
    return render_template("recipys.html", recipes=mongo.db.recipes.find(), title="Larder")

#get one recipe
@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):
    #get last page url from request
    last_page = request.referrer
    #the recipe chosen by the user
    recipe_id = recipe_id
    #get the recipes from database
    recipes = mongo.db.recipes 
    #increment the views of the recipe by +1 in database
    recipes.find_one_and_update(
        {'_id': ObjectId(recipe_id)},
        {'$inc': {'views': 1}}
    )
    #return the recipe details from the database
    recipe = recipes.find_one({'_id': ObjectId(recipe_id)})
    #got to recipe page with recipe details
    return render_template("recipe.html", recipe=recipe, title="ReciPy", last_page=last_page)

#add recipy page
@app.route('/add_recipy', methods=['GET', 'POST'])
def add_recipy():
    #get the form
    form = Add_Recipe(request.form, csrf_enabled=False)
    #if add button pressed
    if form.validate_on_submit():
        # set the collection
        recipes_db = mongo.db.recipes
        #save new recipe in the database
        recipes_db.insert_one({
            'creator': session['username'],
            'title': request.form['title'],
            'description': request.form['description'],
            'ingredients': request.form['ingredients'],
            'instructions': request.form['instructions'],
            'tags': request.form['tags'],
            'imageLink': request.form['imageLink'],
            'views': 1
            })
        #got to myrecips page
        return redirect(url_for('my_recipys', title='SAVED!'))
    #render blank page to fill out
    return render_template('add_recipy.html', form=form, title='Add ReciPy')

#edit recipy page
@app.route('/edit_recipy/<recipe_id>', methods=['GET', 'POST'])
def edit_recipy(recipe_id):
    #get last page url from request
    last_page = request.referrer
    #logged in users can edit their own recipys
    recipe = mongo.db.recipes.find_one_or_404({'_id': ObjectId(recipe_id)})
    #if page is getting info for page
    if request.method == 'GET':
        #get the form
        form = Edit_Recipe(data=recipe)
        #get the details of the recipe to edit
        return render_template('edit_recipy.html', recipe=recipe, form=form, last_page=last_page, title="Edit ReciPy")
    #get the form
    form = Edit_Recipe(request.form)
    #if submit button is pressed
    if form.validate_on_submit():
        #get the recipes from database
        recipes = mongo.db.recipes
        #save the edited details of recipe to database
        recipes.update_one({
            '_id': ObjectId(recipe_id),
        }, {
            '$set': {
                'title': request.form['title'],
                'description': request.form['description'],
                'ingredients': request.form['ingredients'],
                'instructions': request.form['instructions'],
                'tags': request.form['tags'],
                'imageLink': request.form['imageLink'],
            }
        })
        #save the details of the recipe to database
        return redirect(url_for('my_recipys', title="SAVED!"))
        #redirect to try again
    return render_template('edit_recipy.html', recipe=recipe, form=form, last_page=last_page, title="Edit ReciPy")



#confirm delete recipy page
@app.route('/delete_confirmation/<recipe_id>')
def delete_confirmation(recipe_id):
    #get last page url from request
    last_page = request.referrer
    #find the recipe in database and confirm before delete
    recipe = mongo.db.recipes.find_one({'_id': ObjectId(recipe_id)})
    #confirm before delete
    return render_template('delete_recipy.html', title="CONFIRM!", recipe=recipe, last_page=last_page)
 
#delete and return to my recipy page
@app.route('/delete/<recipe_id>')
def delete(recipe_id):
    #get the recipes from database
    recipes = mongo.db.recipes
    #delete the recipe chosen from the database
    recipes.delete_one({
        '_id': ObjectId(recipe_id),
    })
    #redirect to myrecipys
    return redirect(url_for('my_recipys', title="DELETED!"))  

#search for recipes from home screen
@app.route('/search_recipes')
def search_recipes():
    #get value from the search box
    chosenRecipe = request.args['chosenWord']
    #using regular expression to search for exact expresions
    searchInput = {'$regex': re.compile('\W*({})\W*'.format(chosenRecipe)), '$options': 'i'}
    #search recipes in DB for the word in title, tags or ingredients
    results = mongo.db.recipes.find({
        '$or': [
            {'title': searchInput},
            {'tags': searchInput},
            {'ingredients': searchInput},
        ]
    })
    #go to results page 
    return render_template('searchresults.html', query=chosenRecipe, results=results, title="Results")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=false)
        # Successfully connected to heroku
