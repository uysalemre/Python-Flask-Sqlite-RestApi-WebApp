from flask_wtf import RecaptchaField,FlaskForm
from flask_wtf.file import FileField, FileRequired,FileAllowed
from wtforms import StringField,PasswordField,TextAreaField,SelectField,IntegerField
from wtforms.validators import InputRequired,Email,length,URL

#############--------------------------------------ADMIN CREATION FORM---------------------------------------------------###################

class CreateAdminForm(FlaskForm):
    username = StringField("ADMIN NAME", validators=[InputRequired("REQUIRED")])
    email = StringField("ADMIN EMAIL", validators=[InputRequired("REQUIRED"),Email("GIVE A VALID EMAIL")])
    password = PasswordField("PASSWORD", validators=[InputRequired("REQUIRED")])
    passwordAgain = PasswordField("PASSWORD CONFIRM", validators=[InputRequired("REQUIRED")])
    appname = StringField("APP NAME", validators=[InputRequired("REQUIRED")])

class ChangeEmailForm(FlaskForm):
    email=StringField("EMAIL",validators=[InputRequired("EMAIL IS REQUIRED"), Email("PLEASE GIVE A VALID EMAIL")])
    confirmemail=StringField("EMAIL",validators=[InputRequired("EMAIL IS REQUIRED"), Email("PLEASE GIVE A VALID EMAIL")])


class ApplyForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired("Required")])
    surname = StringField("Surname", validators=[InputRequired("Required")])
    email = StringField("EMAIL", validators=[InputRequired("REQUIRED"), Email("GIVE A VALID EMAIL")])
    category = SelectField("Category", choices=[], coerce=str)
    gender = SelectField("GENDER", choices=[], coerce=str)
    age = IntegerField("Age",validators=[InputRequired("Required")])
    phone = IntegerField("Phone", validators=[InputRequired("Required")])
    height = IntegerField("height", validators=[InputRequired("Required")])
    weight = IntegerField("weight", validators=[InputRequired("Required")])
    bodycolor = SelectField("bodycolor", choices=[], coerce=str)
    eyecolor = SelectField("eyecolor", choices=[], coerce=str)
    haircolor = SelectField("haircolor", choices=[], coerce=str)
    hairtype = SelectField("hairtype", choices=[], coerce=str)
    top = IntegerField("Top", validators=[InputRequired("Required")])
    middle = IntegerField("middle", validators=[InputRequired("Required")])
    bottom = IntegerField("bottom", validators=[InputRequired("Required")])
    foot = IntegerField("foot", validators=[InputRequired("Required")])
    facebook = StringField("Facebook",validators=[URL("You must have social media accounts")])
    instagram = StringField("Instagram",validators=[URL("You must have social media accounts")])
    twitter = StringField("Twitter", validators=[URL("You must have social media accounts")])
    description = TextAreaField("description", validators=[InputRequired("Description is required")])
    photo1 = FileField("photo1", validators=[FileRequired(),FileAllowed(['jpg','png'])])
    photo2 = FileField("photo2", validators=[FileRequired(),FileAllowed(['jpg', 'png'])])
    photo3 = FileField("photo3", validators=[FileRequired(),FileAllowed(['jpg', 'png'])])
    photo4 = FileField("photo4", validators=[FileRequired(),FileAllowed(['jpg', 'png'])])
    photo5 = FileField("photo5", validators=[FileRequired(),FileAllowed(['jpg', 'png'])])
    photo6 = FileField("photo6", validators=[FileRequired(),FileAllowed(['jpg', 'png'])])
    photo7 = FileField("photo7", validators=[FileRequired(),FileAllowed(['jpg', 'png'])])
    photo8 = FileField("photo8", validators=[FileRequired(),FileAllowed(['jpg', 'png'])])
    photo9 = FileField("photo9", validators=[FileRequired(),FileAllowed(['jpg', 'png'])])
    photo10 = FileField("photo10", validators=[FileRequired(),FileAllowed(['jpg', 'png'])])




#########-------------------------LOGIN FORM AND RESET PASSWORD OPERATION-------------------################

class LoginForm(FlaskForm):
    email = StringField("EMAIL",validators=[InputRequired("EMAIL IS REQUIRED"), Email("PLEASE GIVE A VALID EMAIL")])
    passw = PasswordField("PASSWORD",validators=[InputRequired("PASSWORD IS REQUIRED")])


class SignUpForm(FlaskForm):
    username = StringField("NAME", validators=[InputRequired("REQUIRED")])
    email = StringField("EMAIL", validators=[InputRequired("REQUIRED"), Email("GIVE A VALID EMAIL")])
    password = PasswordField("PASSWORD", validators=[InputRequired("REQUIRED")])
    passwordAgain = PasswordField("PASSWORD CONFIRM", validators=[InputRequired("REQUIRED")])


class ResetPassword(FlaskForm):
    email=StringField("EMAIL",validators=[InputRequired("EMAIL IS REQUIRED"), Email("PLEASE GIVE A VALID EMAIL")])

class ResetPasswordSubmit(FlaskForm):
    password=PasswordField("PASSWORD",validators=[InputRequired("PASSWORD IS REQUIRED")])
    confirm=PasswordField("CONFIRM PASSWORD",validators=[InputRequired("CONFIRMATION IS REQUIRED")])

############----------------------ADMIN PANEL FORMS AND CRUD OPS WITH THESE FORMS--------------------#################

class SendEmail(FlaskForm):
    mail = SelectField("MAIL", choices=[], coerce=str)
    konu=StringField("SUBJECT")
    mesaj=TextAreaField("MESSAGE",validators=[InputRequired("MESSAGE IS REQUIRED")])
    file=FileField("FILE", validators=[FileAllowed(['docx','xls','pdf','csv','png','jpg','jpeg'])])

class SearchForm(FlaskForm):
    name = StringField("Name")
    surname = StringField("Surname")

#############--------------------------------------CONTACT FORM---------------------------------------------------###################

class ContactForm(FlaskForm):
    name=StringField("NAME-SURNAME",validators=[InputRequired("Name is required")])
    email=StringField("EMAİL",validators=[InputRequired("Email is required"),Email("Give a valid e mail")])
    subject=StringField("SUBJECT",validators=[InputRequired("subject is required")])
    message=TextAreaField("MESSAGE",validators=[InputRequired("message is required")])
    file=FileField("PDF OR DOCX FILE",validators=[FileAllowed(['docx','pdf'],'SADECE DOCX VEYA PDF DOSYASI GEÇERLİDİR.')])