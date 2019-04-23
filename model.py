from wtforms import Form, SelectField, validators

class SimpleForm(Form):
  
	gender = SelectField('Gender', choices=[(0, 'F'), (1, 'M')],
			validators=[validators.InputRequired()])

	ethnicity = SelectField('Race', choices=[(0, 'American Indian/Native Alaskan'),	(1, 'East/South East Asian'), (2, 'Black'), (3, 'Hispanic'), (4, 'Middle East'), (6, 'Other'), (7, 'Unknown')],
			validators=[validators.InputRequired()])
