import os

class MongoDBConfig:
    PWconfig = os.environ.get('MONGO_URI') or 'this-password-is-hidden'
