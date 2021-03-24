from flask_wtf import FlaskForm
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import (StringField, TextAreaField, SelectField,
                     IntegerField, DecimalField, SubmitField)


class PropertyForm(FlaskForm):
    property_title = StringField(
        'Property Title', validators=[InputRequired()])
    description = TextAreaField(
        'Property Description', validators=[InputRequired()],
        render_kw={"rows": 8, "cols": 50})
    no_bedrooms = IntegerField('No. of Bedrooms', validators=[InputRequired()])

    property_type = SelectField('Property Type', choices=[
        ('house', 'House'),
        ('apartment', 'Apartment')
    ])
    no_bathrooms = IntegerField(
        'No. of Bathrooms', validators=[InputRequired()])
    price = DecimalField('Price', validators=[InputRequired()])
    location = StringField(validators=[InputRequired()])
    photo = FileField('Property Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'JPG and PNG Images only!')
    ])
    submit = SubmitField("Add Property")
