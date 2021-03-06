# -*- coding:utf-8 -*-  
'''
__author__:liubin 

'''

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField,SubmitField
from wtforms.validators import DataRequired, Length, Email,Regexp,EqualTo
from wtforms import ValidationError
from ..models import User

#登陆表单
class LoginForm(FlaskForm):

    email = StringField('Email',validators=[DataRequired(), Length(1,64),Email()])
    password = PasswordField('Password',validators=[DataRequired()])

    remember_me = BooleanField('Keep me logged in')

    submit = SubmitField('Log In')

#注册表单

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Length(1,64),
                                             Email()])
    username = StringField('Username',validators=[DataRequired(),Length(1,64),Regexp('^[A-Za-z][A-Aa-z0-9_.]*$',0,
                                                                                     'Usernames must have only letters,'
                                                                                     'numbers,dots or underscores')])
    password = PasswordField('Password',validators=[DataRequired(),EqualTo('password2',message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self,field):

        if User.query.filter_by(username=field.data).first():

            raise ValidationError('Username already in use.')

#修改密码
class ChangePasswordForm(FlaskForm):

    old_password = PasswordField('Old passwpd', validators=[DataRequired()])
    password = PasswordField('New password', validators=[DataRequired(), EqualTo('password2',message='Passwords must match')])
    password2 = PasswordField('Confirm new password', validators=[DataRequired()])
    submit = SubmitField('Update Password')

#重置密码表单
class PasswordResetRequestForm(FlaskForm):

    email = StringField('Email',validators=[DataRequired(),Length(1,64),Email()])
    submit = SubmitField('Reset Password')



class PasswordResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Length(1,64),Email()])

    password = PasswordField('new Password', validators=[DataRequired(),EqualTo('password2',message='Passwords must match')])

    password2 = PasswordField('Confirm password',validators=[DataRequired()])
    submit = SubmitField('Reset Password')


    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first() is None:
            raise ValidationError('Unknown email address.')


#修改邮箱表单
class ChangeEmailForm(FlaskForm):

    email = StringField('New Email',validators=[DataRequired(),Length(1,64),Email()])

    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Update Email Address')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')












