from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from app.models.user import User
from app import db
from app.forms.auth_forms import LoginForm, RegisterForm, UpdatePasswordForm
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import or_

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        account = form.username.data
        user = User.query.filter(or_(User.username == account, User.email == account)).first()

        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('main.index'))
        else:
            flash('用户名/邮箱或密码错误')
    return render_template('login.html', form=form)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('注册成功')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@bp.route('/updatepsw', methods=['GET', 'POST'])
@login_required
def updatepsw():
    form = UpdatePasswordForm()
    if form.validate_on_submit():
        if not check_password_hash(current_user.password, form.old_password.data):
            flash('原密码错误')
        else:
            current_user.password = generate_password_hash(form.new_password.data)
            db.session.commit()
            flash('密码修改成功，请重新登录')
            return redirect(url_for('auth.logout'))
    return render_template('update_password.html', form=form)