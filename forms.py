
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class Add_Recipe(FlaskForm):  
    creator = StringField('Creator', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    ingredients = TextAreaField('Ingredients', validators=[DataRequired()])
    instructions = TextAreaField('Instructions', validators=[DataRequired()])
    tags = StringField('Tags', validators=[DataRequired()])
    imageLink = StringField('Image URL', validators=[DataRequired()])
    submit = SubmitField('Add ReciPy', id="add-recipy-btn")
