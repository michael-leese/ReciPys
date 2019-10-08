#add useful dependencies
import os
from flask import Flask
from bson.objectid import ObjectId
from flask_pymongo import PyMongo

app = Flask(__name__)

PWconfig = os.environ.get('PWMongoDB')

app.config["MONGO_DBNAME"] = 'myRecipeDB'
app.config["MONGO_URI"] = 'mongodb+srv://root:' + PWconfig + '@recipys-giedu.mongodb.net/admin?retryWrites=true&w=majority'

mongo = PyMongo(app)

#Setup simple message to show server setup is working
@app.route('/')
def hello():
    return 'Hello ReciPys!'

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        # Successfully connected to heroku
