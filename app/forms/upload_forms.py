from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed

class YoloUploadForm(FlaskForm):
    image = FileField('上传图片或视频', validators=[
        DataRequired(),
        FileAllowed(['jpg', 'jpeg', 'png', 'bmp', 'mp4', 'avi'], '只能上传图片或视频')
    ])
    submit = SubmitField('上传并识别')

