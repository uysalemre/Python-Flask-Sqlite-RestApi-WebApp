from flask import  Flask
from flask_admin import  Admin
from pages import website
from flask_sqlalchemy import SQLAlchemy
from database import db_session,init_db
from flask_security import Security, SQLAlchemyUserDatastore
from models import *
from datetime import timedelta
from flask_mail import Mail
from pages import AdminView,MyAdminIndexView,MyFileView
import os.path as op

#app = Flask(__name__) # for testing put the app into glo

def create_app():
    app = Flask(__name__)
    app.config.from_object('settings')
    ##------PAGE DEVIDING -----#
    app.register_blueprint(website)
    ##---SECRET KEY -----#
    app.secret_key = app.config.get('secret_key', 'secret')
    ##---MAIL SENDER --##
    app.sender = app.config.get('MAIL_USERNAME')
    app.mail = Mail(app)
    ##--SQL ALCHEMY CONFIGURAION--##
    app.db=SQLAlchemy(app)
    # flask administration
    path = op.join(op.dirname(__file__),'static')
    app.admin = Admin(app, name="Casting Agency" ,template_mode='bootstrap3', index_view=MyAdminIndexView())
    app.admin.add_view(AdminView(Categories, app.db.session))
    app.admin.add_view(AdminView(User, app.db.session,category='User Ops'))
    app.admin.add_view(AdminView(Role, app.db.session,category='User Ops'))
    app.admin.add_view(AdminView(Agency, app.db.session,category='App Manager'))
    app.admin.add_view(AdminView(NormalContact,app.db.session,category='App Manager'))
    app.admin.add_view(AdminView(Setup, app.db.session, category='App Manager'))
    app.admin.add_view(AdminView(StaticNav, app.db.session, category='App Manager'))
    app.admin.add_view(AdminView(Actors, app.db.session, category='Actor Ops'))
    app.admin.add_view(AdminView(ActorBody, app.db.session, category='Actor Ops'))
    app.admin.add_view(AdminView(ActorSoul, app.db.session, category='Actor Ops'))
    app.admin.add_view(AdminView(Photos,app.db.session,category='Actor Ops'))
    app.admin.add_view(AdminView(TempActors, app.db.session, category='Coming Applies'))
    app.admin.add_view(AdminView(TempActorBody, app.db.session, category='Coming Applies'))
    app.admin.add_view(AdminView(TempActorSoul, app.db.session, category='Coming Applies'))
    app.admin.add_view(AdminView(TempPhotos, app.db.session, category='Coming Applies'))
    app.admin.add_view(MyFileView(path, '/static/', name='Static Files'))
    ##--FOR SESSIONS LIFETIME VALUE --##
    app.permanent_session_lifetime=timedelta(hours=10)
    ##-------SETUP FOR FLASK-SECURITY--------##
    app.user_datastore = SQLAlchemyUserDatastore(app.db, User, RolesUsers)
    app.security = Security(app, app.user_datastore)
    ##--REMOVE ALL SESSIONS WHEN PROGRAM ENDED --##
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()
    return app


def main():
    app=create_app()
    host=app.config.get('HOST')
    port=app.config.get('PORT')
    debug=app.config.get('DEBUG')
    app.run(host=host,port=port,debug=debug)

if __name__ == '__main__':
    ##--DB INITIALIZATION--##
    init_db()
    main()