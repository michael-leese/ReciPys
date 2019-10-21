# ReciPys #

Third Milestone Project - Data Centric Development

This project has bought together all the knowledge learnt in the Python and Data Centric Modules that have been covered.  

I have created a recipe storage website utilising the services of Heroku and Mongo DB. 

ReciPy's is the website that allows users to search through all the recipes in our database and see short descriptions of the recipes with an image, to get inspiration. If the user registers they are able to view the full recipe and get the ingredients and instructions to make the meal of their choice.  
The users can add their own recipe to the database, which will be stored in their own dictionary(or Cookopedia) for later so they can quickly see their own recipes. They can edit and delete their own recipes, but dont have the facility to carry out these tasks on anyone elses recipes.

The deployed website is [ReciPys](https://recipys.herokuapp.com).

## UX ##

I have considered the different user experiences as they would move through the site, from whether they are registered users or first time visitors.
New comers who do not wish to register are unable to have access to the full benefits of the site as a registered user would, such as viewing the full recipe or adding one to the users very own recipe dictionary.

See the [Wire Frames](https://github.com/michael-leese/ReciPys/tree/master/wireframes) I used as a basis for my construciton process.

### Features ###

The site has been created offering benefits to the user's who register and log in the ability to store their own recipes in a secure and easy to find place. The users passwordas are stored in an encrypted format that cannot be seen by the DBA. The user can search through other peoples recipes in order to get inspiration, if logged in they can view the full recipe.
Users are able to add and edit their recipes as time goes on by clicking on their recipe and the dynamically added buttons will be available to them.
Other users are unable to access the edit/delete funcitonality of recipes unless they are the creator of the recipe.

#### Features for future Implementation ####

In the future, I would like to add the ability of searching your own recipes as well as providing the ability to link through to the ingredients at a supermarket.

## Technologies Used ##

In this project I have used the following technologies in order to create the website, I have used HTML5 with Jinja Templating and some JQuery and Javascript in order to style the dynamic elements of the page such as buttons and forms:  
Used | <span style="color:white"></span>       
---------- | ----------
Python3 | Jinja Template
HTML5 | CSS3
Bootstrap4 | Javascript
JQuery | MarkDown
Bash | Ubuntu
GIT | GitHub
VS Code | <span style="color:white"></span>

In the [requirements.txt](https://github.com/michael-leese/ReciPys/blob/master/requirements.txt) file a list of depenedencies that were utilised in Python3 are recorded.

## Testing ##

A thorough testing process was undertaken manually, going through the user stories as well as testing all functionality and logic through the front end. This involved testing while not logged in and paying particular attention to the authorised access and the logic the links and buttons would play given the level of access granted to the site.

Further testing was carried out on the responsivity of the site across different browsers and platforms in order to ensure that the site maintained its stylings. The items that have been tested with are listed below:
Tested On | <span style="color:white"></span>       
---------- | ----------
Chrome | web-server-for-chrome
FireFox | Microsoft Edge
Safari | Android Device
IoS Device | Windows LapTop
Chrome devTools inc Remote Device Debug | mybrowseraddon.com useragent-switcher 

## Deployment ##

I have hosted the site on Heroku, and git committed my code here, and kept a repository of the code on GitHub pages, which has been deployed directly from the Master Branch, using the app.py in my Procfile as the first file to run, all access to MongoDB database is handled in this file as well as connection to the app and templates.
If the site is to be updated or added to then further commits will automatically add to this branch and update any file changed/moved/deleted, this will also require committing to Heroku to update the server.
After first setting up Heroku and MongoDB I then went about setting up my VS Code environment with all the extensions that it required and then connected my environment to Heroku and MongoDB using the Ubuntu terminal with Bash Script.
A list of the commands that I had used in the Ubuntu terminal is as follows:
* VS Code
    * wsl
    * code .
* Python 3.6
    * python3
* Flask
    * sudo pip3 install Flask
    * sudo pip3 install flask-pymongo
    * sudo pip3 install dnspython
    * sudo pip3 install bcrypt
    * pip3 freeze --local
    * pip3 freeze --local > requirements.txt
    * python3 -m flask run
* Heroku
    * sudo curl https://cli-assets.heroku.com/install.sh | sh
    * heroku --version
    * heroku login -i
    * heroku login
    * sudo heroku git:remote -a recipys
    * git commit -am "heroku setup"
    * git push heroku master
    * heroku --tails
* Create Procfile
    * echo web: python app.py > Procfile

As well as the various GIT commands that we use regualarily in order to commit our code. 

## Credits ##

I have utilised some of the code that was on the Data Centric Mini Project in order to get some of the functionality workign and off the ground, and have built my own logic and functoinality into the game using some of the sources that have been mentioned in this section.
* ### CodeSnippets ###                                             
    * https://www.w3schools.com/bootstrap4/bootstrap_cards.asp
    * https://stackoverflow.com/questions/35868756/how-to-make-bootstrap-4-cards-the-same-height-in-card-columns
    * http://jkorpela.fi/forms/textarea.html
    * https://stackoverflow.com/questions/5971312/how-to-set-environment-variables-in-python
    * https://hackersandslackers.com/the-art-of-building-flask-routes/
    * https://wtforms.readthedocs.io/en/stable/csrf.html
    * https://wtforms.readthedocs.io/en/stable/fields.html
    * https://www.w3schools.com/python/python_mongodb_getstarted.asp
    * https://stackoverflow.com/questions/36250963/limit-and-sort-order-pymongo-and-mongodb
    * https://www.w3schools.com/python/python_mongodb_sort.asp
    * https://stackoverflow.com/questions/9594125/salt-and-hash-a-password-in-python
    * https://www.programcreek.com/python/example/81490/bcrypt.gensalt
    * https://stackoverflow.com/questions/27413248/why-can-bcrypt-hashpw-be-used-both-for-hashing-and-verifying-passwords
    * https://stackoverflow.com/questions/19605150/regex-for-password-must-contain-at-least-eight-characters-at-least-one-number-a
    * https://superuser.com/questions/903168/how-should-i-write-a-regex-to-match-a-specific-word
    * https://www.programcreek.com/python/example/105273/wtforms.validators.Regexp
    * https://github.com/wtforms/wtforms/issues/437
    * https://stackoverflow.com/questions/14277067/redirect-back-in-flask

#### Media ####

All recipes that have been used have been collected from the [BBC Good Food](https://www.bbcgoodfood.com) site and the photos used on the recipes have been taken from the specific recipe page.
Further images were incorporated to help style the site.
* ### Images and Fonts ###   
       * https://pixabay.com/photos/food-salad-italian-tasty-cooking-2068217/
       * https://pixabay.com/photos/cook-food-plate-tableware-courts-366875/
       * https://fonts.google.com/

#### Acknowledgements ####

I got inspiration from [Recipy](https://www.pinterest.co.uk/jamespalmer5/recipy/), although you may think the name is very similar, believe it or not I had already decided that my Website would be Recipe and Python combined to form ReciPys, long before I had come across this site which I though I could make better and provide more features to the user.

###### This project has been created for educational use ######