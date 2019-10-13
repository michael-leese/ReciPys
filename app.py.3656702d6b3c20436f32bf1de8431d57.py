#add useful dependencies
import os
import re
from webconfig import MongoDBConfig
from flask import Flask, render_template, redirect, request, url_for
from bson.objectid import ObjectId
from flask_pymongo import PyMongo
from forms import Add_Recipe

app = Flask(__name__)

Config = MongoDBConfig()
#setup Mongo
app.config["MONGO_DBNAME"] = 'myRecipeDB'
app.config["MONGO_URI"] = Config.PWconfig

mongo = PyMongo(app)

@app.route('/')

#retrieve home page
@app.route('/index')
def index():
    return render_template("index.html", title="Home")

#retrieve user page
@app.route('/my_recipys')
def my_recipys():
    return render_template("myrecipys.html", users=mongo.db.recipes.find(), title="User")

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
        # insert the new recipe
        recipes_db.insert_one({
            'creator': request.form['creator'],
            'title': request.form['title'],
            'description': request.form['description'],
            'ingredients': request.form['ingredients'],
            'instructions': request.form['instructions'],
            'tags': request.form['tags'],
            'imageLink': request.form['imageLink']
            })
        return redirect(url_for('index', title='SAVED!'))
    return render_template('add_recipe.html', form=form, title='Add ReciPy')

@app.route('/edit_recipe/<recipe_id>', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    """Allows logged in user to edit their own recipes"""
    recipe_db = mongo.db.recipes.find_one_or_404({'_id': ObjectId(recipe_id)})
    if request.method == 'GET':
        form = EditRecipeForm(data=recipe_db)
        return render_template('edit_recipe.html', recipe=recipe_db, form=form)
    form = EditRecipeForm(request.form)
    if form.validate_on_submit():
        recipes_db = mongo.db.recipes
        recipes_db.update_one({
            '_id': ObjectId(recipe_id),
        }, {
            '$set': {
                'creator': request.form['creator'],
            'title': request.form['title'],
            'description': request.form['description'],
            'ingredients': request.form['ingredients'],
            'instructions': request.form['instructions'],
            'tags': request.form['tags'],
            'imageLink': request.form['imageLink']
            }
        })
        return redirect(url_for('index', title='New Recipe Added'))
    return render_template('edit_recipe.html', recipe=recipe_db, form=form)

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
