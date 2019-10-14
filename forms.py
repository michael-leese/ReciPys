
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Email, Regexp 

class Add_Recipe(FlaskForm):  
    creator = StringField('Creator', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    ingredients = TextAreaField('Ingredients', validators=[DataRequired()])
    instructions = TextAreaField('Instructions', validators=[DataRequired()])
    tags = StringField('Tags', validators=[DataRequired()])
    imageLink = StringField('Image URL', validators=[DataRequired()])
    submit = SubmitField('Add ReciPy', id="recipy-btn")

class Registration(FlaskForm):
    regex = "^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{6,20}$"
    PWfailRegexMsg = "Must be 6-20 characters, at least one upper and lower case letter, one number and one special character (@$!%*#?&)"
    nomatch = 'Passwords must match'
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password2', message=nomatch), Regexp(regex=regex, message=PWfailRegexMsg)])
    password2 = PasswordField('Confirm Password')
    firstname = StringField('First name', validators=[DataRequired()])
    lastname = StringField('Last name', validators=[DataRequired()])
    dob = StringField('D.o.B', validators=[DataRequired()])
    email = StringField('Email', validators=[Length(min=6, max=35), Email()])
    submit = SubmitField('Register', id="recipy-btn")