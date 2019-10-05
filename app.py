#add useful dependencies
import os
from flask import Flask

app = Flask(__name__)

#Setup simple message to show server setup is working
@app.route('/')
def hello():
    return 'Hello ReciPys!'

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        # Successfully connected to heroku