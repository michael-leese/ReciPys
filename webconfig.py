import os

class MongoDBConfig:
    PWconfig = os.environ.get('MONGO_URI') or 'this-password-is-hidden'

class PWConfig:
    regex = "^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{6,20}$"
    PWfailRegexMsg = "Must be 6-20 characters, at least one upper and lower case letter, one number and one special character (@$!%*#?&)"

class Keys:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this-key-is-secret'