import os
   
class MongoDBConfig:
    #mongodb credentials
    PWconfig = os.environ.get('MONGO_URI') or 'this-password-is-hidden'

class PWConfig:
    #password regex
    regex = "^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{6,20}$"
    #password error message
    PWfailRegexMsg = "Must be 6-20 characters, at least one upper and lower case letter, one number and one special character (@$!%*#?&)"

class Keys:
    #secret key for flask
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this-key-is-secret'