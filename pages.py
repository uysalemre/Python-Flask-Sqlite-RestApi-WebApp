from flask import Blueprint,render_template,current_app,url_for,request,redirect,abort,session,flash,jsonify,make_response
from flask_security import login_required,logout_user,login_user,current_user,roles_accepted
from passlib.apps import custom_app_context as pwd_content
from models import *
from forms import *
from flask_mail import Message
from itsdangerous import URLSafeTimedSerializer as Serializer
import os, datetime
from functools import wraps
from settings import  roleUser,roleAdmin,adminDescription,guestDescription
from datetime import timedelta
from flask_restful import  Api
from flask_cors import CORS
from api.sources import ActorsListApi
from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView,expose
from flask_admin.contrib.fileadmin import FileAdmin



website = Blueprint('website',__name__)
api = Api(website)
CORS(website)


def setup_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        pass_setup = Setup.query.filter_by(id=1).first()
        if pass_setup is None:
            return redirect(url_for('website.setup', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


@setup_required
def getNavBar():
    app = Setup.query.filter_by(id=1).first()
    categories = Categories.query.all()
    actors = Actors.query.filter_by(activated=True).all()
    modeling = ActorModel.query.all()
    staticLink = StaticNav.query.filter_by(activated=True).all()
    return app,categories,actors,modeling,staticLink


def send_password_reset_email(user_email):
    password_reset_serializer = Serializer(current_app.config['SECRET_KEY'])
    password_reset_url = url_for('website.reset_with_token',token=password_reset_serializer.dumps(user_email, salt=current_app.config['SECURITY_PASSWORD_SALT']), _external=True)
    link=password_reset_url
    with current_app.mail.connect() as conn:
        msg=Message(subject='RESET PASSWORD',body=link,sender=current_app.sender,recipients=[user_email])
        conn.send(msg)


def send_apply_message(user_email,message):
    with current_app.mail.connect() as conn:
        msg = Message(subject='CASTING APPLICATION', body=message, sender=current_app.sender, recipients=[user_email])
        conn.send(msg)


@website.route('/',methods=['GET','POST'])
def setup():
    form = CreateAdminForm()
    time = datetime.datetime.now()

    setted = Setup.query.filter_by(id=1).first()
    if setted is not None:
        return redirect(url_for('website.home'))

    if request.method == "POST" and form.validate_on_submit():
        username = form.username.data
        appname = form.appname.data
        email = form.email.data
        if form.password.data != form.passwordAgain.data:
            flash('Passwords are not same')
            return redirect(url_for('website.setup'))
        current_app.db.session.add(User(email,username,pwd_content.encrypt(form.password.data),True,time))
        current_app.db.session.add(Setup(appname,True))
        current_app.db.session.add(Role(roleAdmin, adminDescription))
        current_app.db.session.add(Role(roleUser, guestDescription))
        current_app.db.session.commit()
        user_id = User.query.filter_by(email=email).first()
        role_id = Role.query.filter_by(name=roleAdmin).first()
        current_app.db.session.add(RolesUsers(user_id.id, role_id.id))
        current_app.db.session.commit()
        return redirect(url_for('website.home'))
    return render_template('setup.html',form=form)


@website.route('/home',methods=['GET','POST'])
@setup_required
def home():
    app,categories,actors,modeling,staticLink = getNavBar()
    photo = Photos.query.all()
    return render_template('mainpages/home.html',appName=app.appname,categories=categories,actors=actors,modeling=modeling,staticLink=staticLink,photo=photo)


@website.route('/apply', methods=['GET','POST'])
@setup_required
def apply():
    app, categories, actors, modeling, staticLink = getNavBar()
    form = ApplyForm()
    cats = Categories.query.all()
    form.category.choices = [(k.name, k.name) for k in cats]
    gender = ['BOY','GIRL']
    form.gender.choices = [(k,k) for k in gender]
    bodycolor = ['BLACK','WHITE']
    form.bodycolor.choices = [(k, k) for k in bodycolor]
    haircolor = ['BLONDE','BLACK','RED']
    form.haircolor.choices = [(k, k) for k in haircolor]
    hairtype = ['CURLY','STRAIGHT','WAVY']
    form.hairtype.choices = [(k, k) for k in hairtype]
    eyecolor = ['BLUE','BLACK','BROWN','GREEN','HAZEL']
    form.eyecolor.choices = [(k,k) for k in eyecolor]
    if form.validate_on_submit() and request.method == "POST":
        actorfirst = TempActors.query.filter_by(email=form.email.data).first()
        if actorfirst:
            flash("This email applied before.")
            return redirect(url_for('website.apply'))
        photo1 = form.photo1.data
        photo2 = form.photo2.data
        photo3 = form.photo3.data
        photo4 = form.photo4.data
        photo5 = form.photo5.data
        photo6 = form.photo6.data
        photo7 = form.photo7.data
        photo8 = form.photo8.data
        photo9 = form.photo9.data
        photo10 = form.photo10.data
        os.mkdir('static/actorphotos/'+form.email.data+'')
        photo1.save(os.path.join('static/actorphotos/'+form.email.data+'', photo1.filename)) if photo1 else None
        photo2.save(os.path.join('static/actorphotos/'+form.email.data+'', photo2.filename)) if photo2 else None
        photo3.save(os.path.join('static/actorphotos/'+form.email.data+'', photo3.filename)) if photo3 else None
        photo4.save(os.path.join('static/actorphotos/'+form.email.data+'', photo4.filename)) if photo4 else None
        photo5.save(os.path.join('static/actorphotos/'+form.email.data+'', photo5.filename)) if photo5 else None
        photo6.save(os.path.join('static/actorphotos/'+form.email.data+'', photo6.filename)) if photo6 else None
        photo7.save(os.path.join('static/actorphotos/'+form.email.data+'', photo7.filename)) if photo7 else None
        photo8.save(os.path.join('static/actorphotos/'+form.email.data+'', photo8.filename)) if photo8 else None
        photo9.save(os.path.join('static/actorphotos/'+form.email.data+'', photo9.filename)) if photo9 else None
        photo10.save(os.path.join('static/actorphotos/'+form.email.data+'', photo10.filename)) if photo10 else None
        current_app.db.session.add(TempActors(form.name.data, form.surname.data, form.email.data, False, form.gender.data, form.age.data,form.phone.data))
        current_app.db.session.commit()
        actor = TempActors.query.filter_by(email=form.email.data).first()
        current_app.db.session.add(TempActorBody(actor.id, form.height.data, form.weight.data, form.bodycolor.data, form.haircolor.data,form.hairtype.data, form.eyecolor.data, form.top.data, form.middle.data, form.bottom.data,form.foot.data))
        current_app.db.session.add(TempActorSoul(actor.id, form.facebook.data, form.twitter.data, form.instagram.data, form.description.data))
        category_id = Categories.query.filter_by(name=form.category.data).first()
        current_app.db.session.add(TempActorModel(actor.id,category_id.id))
        current_app.db.session.add(TempPhotos(actor.id,photo1.filename,photo2.filename,photo3.filename,photo4.filename,photo5.filename,photo6.filename,photo7.filename,photo8.filename,photo9.filename,photo10.filename))
        current_app.db.session.commit()
        send_apply_message(form.email.data)
        flash('Application Completed Successfully')
        return redirect(url_for('website.apply'))
    return render_template('mainpages/apply.html',appName=app.appname,categories=categories,actors=actors,modeling=modeling,staticLink=staticLink,form=form)


@website.route('/contact',methods = ['GET','POST'])
@setup_required
def contact():
    app, categories, actors, modeling, staticLink = getNavBar()
    form = ContactForm()
    if form.validate_on_submit() and request.method == "POST":
        last_email = NormalContact.query.order_by(NormalContact.time.desc()).first()
        if last_email:
            if last_email.email==form.email.data and last_email.time + timedelta(seconds=120) >= datetime.datetime.now():
                flash("You are not allowed to send message again in a 2 minutes ")
                return redirect(url_for('website.contact'))
        file = form.file.data
        if file:
            file.save(os.path.join('static/contactfiles/',file.filename))
            current_app.db.session.add(NormalContact(form.name.data,form.email.data,form.subject.data,form.message.data,file.filename,datetime.datetime.now()))
        current_app.db.session.add(NormalContact(form.name.data, form.email.data, form.subject.data, form.message.data,None,datetime.datetime.now()))
        current_app.db.session.commit()
        flash("Thanks for contact with us")
        send_apply_message(form.email.data,"Your contact message reached us we will make a detailed information to you in next days.")
        return redirect(url_for('website.contact'))
    return render_template('mainpages/contact.html',appName=app.appname,categories=categories,actors=actors,modeling=modeling,staticLink=staticLink,form=form)


@website.route('/login',methods = ['GET','POST'])
@setup_required
def login():
    app, categories, actors, modeling, staticLink = getNavBar()
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        passw = form.passw.data
        user = User.query.filter_by(email=email, active=1).first()
        if user and pwd_content.verify(passw, user.password) and user.has_role('Guest'):
            session[user.username] = user.username
            login_user(user)
            current_app.db.session.query(User).filter_by(email=email).update({User.last_time: datetime.datetime.now()})
            Logs(request.remote_addr, user.email)
            current_app.db.session.commit()
            return redirect(url_for('website.home'))
        else:
            flash(" Wrong email or password ")
            return redirect(url_for('website.login'))
    return render_template('auth/login.html',appName=app.appname,categories=categories,actors=actors,modeling=modeling,staticLink=staticLink,form=form)


@website.route('/signup',methods = ['GET','POST'])
@setup_required
def signup():
    app, categories, actors, modeling, staticLink = getNavBar()
    form = SignUpForm()
    if form.validate_on_submit() and request.method == "POST":
        existing = User.query.filter_by(email=form.email.data).first()
        if existing:
            flash("This Company already signed up")
            return redirect(url_for('website.signup'))
        if form.password.data != form.passwordAgain.data:
            flash("Passwords are not same try again")
            return redirect(url_for('website.signup'))
        current_app.db.session.add(User(form.email.data,form.username.data,pwd_content.encrypt(form.password.data),False,datetime.datetime.now()))
        current_app.db.session.commit()
        this = User.query.filter_by(email=form.email.data).first()
        current_app.db.session.add(RolesUsers(this.id,2))
        current_app.db.session.commit()
        send_apply_message(form.email.data,"Thanks for sign-up we will email you about auth after check your account")
        flash("Hello {} thanks for signed up after checking your account we will email you about your auth ".format(form.username.data))
    return render_template('auth/signup.html',appName=app.appname,categories=categories,actors=actors,modeling=modeling,staticLink=staticLink,form=form)




@website.route('/profile',methods=['GET','POST'])
@setup_required
@login_required
@roles_accepted('Guest')
def profile():
    app, categories, actors, modeling, staticLink = getNavBar()
    return render_template('mainpages/profile.html',appName=app.appname,categories=categories,actors=actors,modeling=modeling,staticLink=staticLink)


@website.route('/forgotpassword',methods=['GET','POST'])
@setup_required
def forgotpassword():
    app, categories, actors, modeling, staticLink = getNavBar()
    form = ResetPassword()
    if form.validate_on_submit() and request.method == "POST":
        exists = User.query.filter_by(email=form.email.data,active=1).first()
        if not exists:
            flash("This is not authorized email")
            return redirect(url_for('website.login'))
        send_password_reset_email(exists.email)
        flash("We have sent a email to you ")
        return redirect(url_for('website.login'))
    return render_template('auth/forgotpassword.html',appName=app.appname,categories=categories,actors=actors,modeling=modeling,staticLink=staticLink,form=form)


@website.route('/reset/<token>', methods=["GET", "POST"])
@setup_required
def reset_with_token(token):
    try:
        password_reset_serializer = Serializer(current_app.config['SECRET_KEY'])
        email = password_reset_serializer.loads(token, salt=current_app.config['SECURITY_PASSWORD_SALT'], max_age=60)
    except:
        return redirect(url_for('website.login'))
    form = ResetPasswordSubmit()
    if request.method == 'POST' and form.validate_on_submit():
        girilen = form.password.data
        onaylanacak = form.confirm.data
        if girilen == onaylanacak:
            current_app.db.session.query(User).filter(User.email == email).update({User.password: pwd_content.encrypt(girilen)})
            current_app.db.session.commit()
            flash("Password Changed")
            return redirect(url_for('website.login'))
        flash("Please check the passwords. They are not same")
    return render_template('auth/reset_with_token.html', form=form)


@website.route('/logout',methods = ['GET'])
@setup_required
@login_required
@roles_accepted('Guest')
def logout():
    if not current_user.is_authenticated:
        return redirect(url_for('website.home'))
    session.pop(current_user.username)
    logout_user()
    return redirect(url_for('website.home'))


@website.route('/logout-admin',methods = ['GET'])
@setup_required
@login_required
@roles_accepted('Admin')
def adminlogout():
    if not current_user.is_authenticated:
        return redirect(url_for('website.home'))
    session.pop(current_user.email)
    logout_user()
    return redirect(url_for('website.home'))



@website.route('/categories/<string:category>',methods=['GET'])
@setup_required
def category(category):
    existCheck = Categories.query.filter_by(name=category).first()
    if not existCheck:
        abort(404)
    app, categories, actors, modeling, staticLink = getNavBar()
    photo = Photos.query.all()
    return render_template('mainpages/category.html',appName=app.appname,categories=categories,actors=actors,modeling=modeling,staticLink=staticLink,existCheck=existCheck,photo=photo)


@website.route('/<string:category>/<int:id>',methods=['GET'])
@setup_required
def model(category,id):
    actor = Actors.query.filter_by(id=id).first()
    existCheck = Categories.query.filter_by(name=category).first()
    if existCheck:
        model = ActorModel.query.filter_by(user_id=id,category_id = existCheck.id).first()
        if not model or actor.activated == False:
            abort(404)
    app, categories, actors, modeling, staticLink = getNavBar()
    photo = Photos.query.filter_by(user_id=id).first()
    soul = ActorSoul.query.filter_by(user_id=id).first()
    body = ActorBody.query.filter_by(user_id=id).first()
    return render_template('mainpages/model.html',appName=app.appname,categories=categories,actors=actors,modeling=modeling,staticLink=staticLink,actor=actor,photo=photo,soul=soul,body=body)


@website.route('/admin-login',methods=['GET','POST'])
@setup_required
def adminlogin():
        form = LoginForm()
        if request.method == "POST" and form.validate_on_submit():
            email = form.email.data
            passw = form.passw.data
            user = User.query.filter_by(email=email, active=1).first()
            if user:
                if user.has_role('Admin') and pwd_content.verify(passw, user.password):
                    session[user.email] = user.email
                    login_user(user)
                    current_app.db.session.query(User).filter_by(email=email).update({User.last_time: datetime.datetime.now()})
                    current_app.db.session.commit()
                    Logs(request.remote_addr, user.email)
                    return redirect('/admin/')
                flash(" You are not authorized ")
            flash(" You are not authorized")
        return render_template('admin/login.html', form=form)


@website.route('/about-us',methods=['GET'])
@setup_required
def aboutus():
    app, categories, actors, modeling, staticLink = getNavBar()
    agency = Agency.query.filter_by(id=1).first()
    return render_template('mainpages/aboutus.html',appName=app.appname,categories=categories,actors=actors,modeling=modeling,staticLink=staticLink,agency=agency)


class AdminView(ModelView):

    def is_accessible(self):
        if not current_user.is_active or not current_user.is_authenticated:
            return False
        if current_user.has_role('Admin'):
            return True
        return False

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            if current_user.is_authenticated:
                abort(403)
            else:
                return redirect(url_for('website.adminlogin'))


class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        return self.render('admin/index.html')

    def is_accessible(self):
        if not current_user.is_active or not current_user.is_authenticated:
            return False
        if current_user.has_role('Admin'):
            return True
        return False

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            if current_user.is_authenticated:
                abort(403)
            else:
                return redirect(url_for('website.adminlogin'))


class MyFileView(FileAdmin):
    def is_accessible(self):
        if not current_user.is_active or not current_user.is_authenticated:
            return False
        if current_user.has_role('Admin'):
            return True
        return False

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            if current_user.is_authenticated:
                abort(403)
            else:
                return redirect(url_for('website.adminlogin'))

api.add_resource(ActorsListApi,'/api/v1.0/models',endpoint='models')


