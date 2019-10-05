#add useful dependencies
import os
import config
from flask import Flask
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

PWconfig = config.DBSettings['DBPassword']

app.config["MONGO_DBNAME"] = 'myRecipeDB'
app.config["MONGO_URI"] = 'mongodb+srv://root:' + PWconfig + '@recipys-giedu.mongodb.net/admin?retryWrites=true&w=majority'

#Setup simple message to show server setup is working
@app.route('/')
def hello():
    return 'Hello ReciPys!'

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        # Successfully connected to heroku