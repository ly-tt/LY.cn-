from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from flask_wtf.file import FileRequired, FileAllowed

class AudioUploadForm(FlaskForm):
    audio = FileField('上传语音（mp3/wav）', validators=[
        FileRequired(),
        FileAllowed(['wav', 'mp3', 'webm'], '只支持 wav、mp3、webm 格式')
    ])
    submit = SubmitField('识别语音')
