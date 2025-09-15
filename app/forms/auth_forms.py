from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo ,Email

class LoginForm(FlaskForm):
    username = StringField('用户名/邮箱', validators=[DataRequired(message='请输入用户名/邮箱')])
    password = PasswordField('密码', validators=[DataRequired(message='请输入密码')])
    submit = SubmitField('登录')

class RegisterForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('邮箱', validators=[DataRequired(message='请输入邮箱')])
    password = PasswordField('密码', validators=[DataRequired(), Length(min=6, message='密码至少6位')])
    confirm_password = PasswordField('确认密码', validators=[
        DataRequired(),
        EqualTo('password', message='两次密码不一致')
    ])
    submit = SubmitField('注册')

class UpdatePasswordForm(FlaskForm):
    old_password = PasswordField('原密码', validators=[DataRequired()])
    new_password = PasswordField('新密码', validators=[DataRequired(), Length(min=6, message='新密码至少6位')])
    confirm_password = PasswordField('确认新密码', validators=[
        DataRequired(),
        EqualTo('new_password', message='两次密码不一致')
    ])
    submit = SubmitField('修改密码')

