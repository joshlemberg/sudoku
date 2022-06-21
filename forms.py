from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange

class CellForm(FlaskForm):
	newingredient = StringField('Ingredient Name', validators=[DataRequired(message="Name of ingredient is required.")])
	cell00 = IntegerField(validators=[NumberRange(min=1, max=9)], default=".")
	submit = SubmitField('Add Ingredient')