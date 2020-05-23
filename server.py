from flask import Flask
from flask_admin import Admin
from pages import website
from flask_sqlalchemy import SQLAlchemy
from database import db_session, init_db, delete_db
from flask_security import Security, SQLAlchemyUserDatastore
from models import *
from datetime import timedelta
from flask_mail import Mail
from pages import AdminView, MyAdminIndexView, MyFileView
import os.path as op


def create_app():
    app = Flask(__name__)
    app.config.from_object('settings')
    app.register_blueprint(website)
    app.secret_key = app.config.get('secret_key', 'secret')
    app.sender = app.config.get('MAIL_USERNAME')
    app.mail = Mail(app)
    app.db = SQLAlchemy(app)
    path = op.join(op.dirname(__file__), 'static')
    app.admin = Admin(app, name="Casting Agency", template_mode='bootstrap3', index_view=MyAdminIndexView())
    app.admin.add_view(AdminView(Categories, app.db.session))
    app.admin.add_view(AdminView(User, app.db.session, category='User Ops'))
    app.admin.add_view(AdminView(Role, app.db.session, category='User Ops'))
    app.admin.add_view(AdminView(Agency, app.db.session, category='App Manager'))
    app.admin.add_view(AdminView(NormalContact, app.db.session, category='App Manager'))
    app.admin.add_view(AdminView(Setup, app.db.session, category='App Manager'))
    app.admin.add_view(AdminView(StaticNav, app.db.session, category='App Manager'))
    app.admin.add_view(AdminView(Actors, app.db.session, category='Actor Ops'))
    app.admin.add_view(AdminView(ActorBody, app.db.session, category='Actor Ops'))
    app.admin.add_view(AdminView(ActorSoul, app.db.session, category='Actor Ops'))
    app.admin.add_view(AdminView(Photos, app.db.session, category='Actor Ops'))
    app.admin.add_view(AdminView(TempActors, app.db.session, category='Coming Applies'))
    app.admin.add_view(AdminView(TempActorBody, app.db.session, category='Coming Applies'))
    app.admin.add_view(AdminView(TempActorSoul, app.db.session, category='Coming Applies'))
    app.admin.add_view(AdminView(TempPhotos, app.db.session, category='Coming Applies'))
    app.admin.add_view(MyFileView(path, '/static/', name='Static Files'))
    app.permanent_session_lifetime = timedelta(hours=10)
    app.user_datastore = SQLAlchemyUserDatastore(app.db, User, RolesUsers)
    app.security = Security(app, app.user_datastore)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    return app


def main():
    app = create_app()
    host = app.config.get('HOST')
    port = app.config.get('PORT')
    debug = app.config.get('DEBUG')
    app.run(host=host, port=port, debug=debug)


if __name__ == '__main__':
    init_db()
    main()
