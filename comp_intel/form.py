from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email


class ChannelForm(FlaskForm):
    name = StringField("Channel: ", validators=[DataRequired()])
    channel = BooleanField('Канал')
    chat = BooleanField('Чат')
    submit = SubmitField("Submit")
