from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed

class OCRForm(FlaskForm):
    image = FileField('上传图片', validators=[
        DataRequired(),
        FileAllowed(['jpg', 'jpeg', 'png'], '只能上传图片')
    ])
    submit = SubmitField('开始识别')
