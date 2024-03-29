from flask import render_template,redirect,url_for,request,flash
from flask_login import current_user,login_user,logout_user,login_required
from . import auth
from ..models import User,Blog,Comment,Category,Subscribe
from .forms import RegistrationForm,LoginForm
from .. import db
from ..email import mail_message


@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('auth.login'))
        title = "New Account"

    return render_template('auth/register.html',registration_form = form)


@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)

            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "Search login"
    return render_template('auth/login.html',login_form = login_form,title = title)

@auth.route('confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        flash("Account Confirmed!")
    else:
        flash("The confirmation link is invalid.")

    return redirect(url_for('main.index'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
