from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class TextAnalysisForm(FlaskForm):
    content = TextAreaField('请输入文本', validators=[DataRequired()])
    submit = SubmitField('分析情感')

