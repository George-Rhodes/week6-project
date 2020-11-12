from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, textAreaFeild
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired, ValidationError
from application.models import Routine



class routeCheck:
	def __init__(self, message):
		self.message = message

	def __call__(self, form, field):
		routineList = Routine.query.all()
		for routine in routineList:
			if routine.rTitle == field.data:
				raise ValidationError(self.message)

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
		validators=[DataRequired(),
		routeCheck(message='routine already exists')])
	author = StringField('Author',
		validators=[DataRequired()])
	description = StringField('Descpriton', widget=TextArea(),
		validators=[DataRequired()])
	submit = SubmitField('Make Routine')


class updateForm(FlaskForm):
	rTitle = StringField('Routine Title',
		validators=[DataRequired(),
		routeCheck(message='routine already exists')])
	author = StringField('Author',
		validators=[DataRequired()])
	description = StringField('Description', widget=TextArea(),
		validators=[DataRequired()])
	submit = SubmitField('Update Routine')
