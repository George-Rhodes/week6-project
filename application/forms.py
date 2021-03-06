from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, IntegerField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired, ValidationError
from application.models import Routine





class orderedForm(FlaskForm):
    orderedWith = SelectField('Order With',
        choices=[
            ("id", "Recent"),
            ("old", "Old")
        ]
    )
    submit = SubmitField('Order')

class routeForm(FlaskForm):
	rTitle = StringField('Routine Title',
		validators=[DataRequired()])
	author = StringField('Author',
		validators=[DataRequired()])
	description = StringField('Descpriton', widget=TextArea(),
		validators=[DataRequired()])
	submit = SubmitField('Make Routine')


class updateForm(FlaskForm):
	rTitle = StringField('Routine Title',
		validators=[DataRequired()])
	author = StringField('Author',
		validators=[DataRequired()])
	description = StringField('Description', widget=TextArea(),
		validators=[DataRequired()])
	submit = SubmitField('Update Routine')


class excerForm(FlaskForm) :
	set_name = StringField('excersise name',
		validators=[DataRequired()])
	level_num = IntegerField('level of excersise',
		validators=[DataRequired()])
	level_type = SelectField('Order With',
        choices=[
            ("Kg", "Kilos"),
            ("Resistance", "Resistance")
        ]
    )
	set_length = IntegerField('length of excersise',
		validators=[DataRequired()])
	set_type = SelectField('Order With',
        choices=[
            ("sets", "set"),
            ("Minutes", "Minutes")
        ]
    )
	submit = SubmitField('Make Excersise')