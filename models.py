from database import Base
from flask_security import UserMixin, RoleMixin
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Boolean, DateTime, Column, Integer, String, ForeignKey, Text
import datetime


class Setup(Base):
    __tablename__ = 'setup'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    appname = Column(String(50),unique=True,nullable=False)
    settted = Column(Boolean(),default=False)

    def __init__(self,appname=None,setted=None):
        self.appname=appname
        self.settted=setted


class RolesUsers(Base):
    __tablename__ = 'roles_users'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    user_id = Column('user_id', Integer(), ForeignKey('user.id'))
    role_id = Column('role_id', Integer(), ForeignKey('role.id'))

    def __init__(self, user_id, role_id):
        self.user_id = user_id
        self.role_id = role_id


class Role(Base, RoleMixin):
    __tablename__ = 'role'
    id = Column(Integer(), primary_key=True)
    name = Column(String(80), unique=True)
    description = Column(String(255))

    def __init__(self, name=None, description=None):
        self.name = name
        self.description = description

    def __repr__(self):
        return self.name


class User(Base, UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), unique=True)
    username = Column(String(255))
    password = Column(String(255))
    active = Column(Boolean())
    last_time = Column(DateTime())
    roles = relationship('Role', secondary='roles_users',backref=backref('users', lazy='dynamic'))

    def __init__(self, email=None, username=None, password=None, active=None, last_time=None):
        self.email = email
        self.username = username
        self.password = password
        self.active = active
        self.last_time = last_time



class Agency(Base):
    __tablename__ = 'agency'
    id = Column(Integer, primary_key=True, autoincrement=True)
    company = Column(String(80), nullable=True)
    phone = Column(Integer(), nullable=True)
    director = Column(String(80), nullable=True)
    photo = Column(Text, nullable=True)
    description = Column(Text, nullable=True)
    instagram = Column(Text, nullable=True)
    facebook = Column(Text, nullable=True)
    twitter = Column(Text, nullable=True)

    def __init__(self, company=None, phone=None, director=None, photo=None, description=None, instagram=None, facebook=None, twitter=None):
        self.company = company
        self.phone = phone
        self.director = director
        self.photo = photo
        self.description = description
        self.instagram = instagram
        self.facebook = facebook
        self.twitter = twitter


class StaticNav(Base):
    __tablename__ = 'staticnav'
    id = Column(Integer, primary_key=True, autoincrement=True)
    header = Column(String(80), nullable=True)
    link = Column(Text, nullable=True)
    activated = Column(Boolean(), default=False)

    def __init__(self, header=None, link=None, activated=None):
        self.header = header
        self.link = link
        self.activated = activated


class NormalContact(Base):
    __tablename__ = 'normalcontact'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80), nullable=True)
    email = Column(Text, nullable=False)
    subject = Column(String(80), nullable=True)
    message = Column(Text, nullable=True)
    document = Column(Text, nullable=True)
    time = Column(DateTime())

    def __init__(self, name=None, email=None, subject=None, message=None, document=None, time=datetime.datetime.now()):
        self.name = name
        self.email = email
        self.subject = subject
        self.message = message
        self.document = document
        self.time = time


class Actors(Base):
    __tablename__ = 'actors'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80), nullable=False)
    surname = Column(String(80), nullable=False)
    email = Column(Text, nullable=False, unique=True)
    activated = Column(Boolean(), default=False)
    gender = Column(String(50), nullable=False)
    age = Column(Integer(), nullable=False)
    phone = Column(Integer(), nullable=False)
    category = relationship('Categories',secondary='actormodel',backref=backref('actors'))

    def __init__(self, name=None, surname=None, email=None, activated=None, gender=None, age=None, phone=None):
        self.name = name
        self.surname = surname
        self.email = email
        self.activated = activated
        self.gender = gender
        self.age = age
        self.phone = phone

    def __repr__(self):
        return self.email


class Categories(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80), nullable=False)
    description = Column(Text)

    def __init__(self, name=None, description=None):
        self.name = name
        self.description = description

    def __repr__(self):
        return self.name


class Photos(Base):
    __tablename__ = 'photos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column('user_id', Integer(), ForeignKey('actors.id'))
    photo1 = Column(Text, default="no-data")
    photo2 = Column(Text, default="no-data")
    photo3 = Column(Text, default="no-data")
    photo4 = Column(Text, default="no-data")
    photo5 = Column(Text, default="no-data")
    photo6 = Column(Text, default="no-data")
    photo7 = Column(Text, default="no-data")
    photo8 = Column(Text, default="no-data")
    photo9 = Column(Text, default="no-data")
    photo10 = Column(Text, default="no-data")
    actor = relationship('Actors', backref=backref('photo'))

    def __init__(self, user_id=None, photo1=None, photo2=None, photo3=None, photo4=None, photo5=None, photo6=None, photo7=None, photo8=None, photo9=None, photo10=None):
        self.user_id = user_id
        self.photo1 = photo1
        self.photo2 = photo2
        self.photo3 = photo3
        self.photo4 = photo4
        self.photo5 = photo5
        self.photo6 = photo6
        self.photo7 = photo7
        self.photo8 = photo8
        self.photo9 = photo9
        self.photo10 = photo10


class ActorBody(Base):
    __tablename__ = 'actorbody'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column('user_id', Integer(), ForeignKey('actors.id'))
    height = Column(String(20), nullable=True)
    weight = Column(String(20), nullable=True)
    bodycolor = Column(String(50), nullable=True)
    haircolor = Column(String(50), nullable=True)
    hairtype = Column(String(50), nullable=True)
    eyecolor = Column(String(50), nullable=True)
    top = Column(Integer(), nullable=True)
    middle = Column(Integer(), nullable=True)
    bottom = Column(Integer(), nullable=True)
    foot = Column(Integer(), nullable=True)
    actor = relationship('Actors',backref=backref('body'))

    def __init__(self, user_id=None, height=None, weight=None, bodycolor=None, haircolor=None, hairtype=None, eyecolor=None, top=None, middle=None, bottom=None, foot=None):
        self.user_id = user_id
        self.height = height
        self.weight = weight
        self.bodycolor = bodycolor
        self.haircolor = haircolor
        self.hairtype = hairtype
        self.eyecolor = eyecolor
        self.top = top
        self.middle = middle
        self.bottom = bottom
        self.foot = foot


class ActorSoul(Base):
    __tablename__ = 'actorsoul'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column('user_id', Integer(), ForeignKey('actors.id'))
    facebook = Column(Text, nullable=True)
    twitter = Column(Text, nullable=True)
    instagram = Column(Text, nullable=True)
    description = Column(Text, nullable=True)
    actor = relationship('Actors', backref=backref('soul'))

    def __init__(self, user_id=None, facebook=None, twitter=None, instagram=None, description=None):
        self.user_id = user_id
        self.facebook = facebook
        self.twitter = twitter
        self.instagram = instagram
        self.description = description



class ActorModel(Base):
    __tablename__ = 'actormodel'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column('user_id', Integer(), ForeignKey('actors.id'))
    category_id = Column('category_id', Integer(), ForeignKey('categories.id'))

    def __init__(self, user_id=None, category_id=None):
        self.user_id = user_id
        self.category_id = category_id


class TempActors(Base):
    __tablename__ = 'Tempactors'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(80), nullable=False)
    surname = Column(String(80), nullable=False)
    email = Column(Text, nullable=False, unique=True)
    activated = Column(Boolean(), default=False)
    gender = Column(String(50), nullable=False)
    age = Column(Integer(), nullable=False)
    phone = Column(Integer(), nullable=False)
    category = relationship('Categories',secondary='Tempactormodel',backref=backref('tempactors'))


    def __init__(self, name=None, surname=None, email=None, activated=None, gender=None, age=None, phone=None):
        self.name = name
        self.surname = surname
        self.email = email
        self.activated = activated
        self.gender = gender
        self.age = age
        self.phone = phone


class TempPhotos(Base):
    __tablename__ = 'Tempphotos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column('user_id', Integer(), ForeignKey('Tempactors.id'))
    photo1 = Column(Text, default="no-data")
    photo2 = Column(Text, default="no-data")
    photo3 = Column(Text, default="no-data")
    photo4 = Column(Text, default="no-data")
    photo5 = Column(Text, default="no-data")
    photo6 = Column(Text, default="no-data")
    photo7 = Column(Text, default="no-data")
    photo8 = Column(Text, default="no-data")
    photo9 = Column(Text, default="no-data")
    photo10 = Column(Text, default="no-data")

    def __init__(self, user_id=None, photo1=None, photo2=None, photo3=None, photo4=None, photo5=None, photo6=None, photo7=None, photo8=None, photo9=None, photo10=None):
        self.user_id = user_id
        self.photo1 = photo1
        self.photo2 = photo2
        self.photo3 = photo3
        self.photo4 = photo4
        self.photo5 = photo5
        self.photo6 = photo6
        self.photo7 = photo7
        self.photo8 = photo8
        self.photo9 = photo9
        self.photo10 = photo10


class TempActorBody(Base):
    __tablename__ = 'Tempactorbody'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column('user_id', Integer(), ForeignKey('Tempactors.id'))
    height = Column(String(20), nullable=True)
    weight = Column(String(20), nullable=True)
    bodycolor = Column(String(50), nullable=True)
    haircolor = Column(String(50), nullable=True)
    hairtype = Column(String(50), nullable=True)
    eyecolor = Column(String(50), nullable=True)
    top = Column(Integer(), nullable=True)
    middle = Column(Integer(), nullable=True)
    bottom = Column(Integer(), nullable=True)
    foot = Column(Integer(), nullable=True)

    def __init__(self, user_id=None, height=None, weight=None, bodycolor=None, haircolor=None, hairtype=None, eyecolor=None, top=None, middle=None, bottom=None, foot=None):
        self.user_id = user_id
        self.height = height
        self.weight = weight
        self.bodycolor = bodycolor
        self.haircolor = haircolor
        self.hairtype = hairtype
        self.eyecolor = eyecolor
        self.top = top
        self.middle = middle
        self.bottom = bottom
        self.foot = foot


class TempActorSoul(Base):
    __tablename__ = 'Tempactorsoul'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column('user_id', Integer(), ForeignKey('Tempactors.id'))
    facebook = Column(Text, nullable=True)
    twitter = Column(Text, nullable=True)
    instagram = Column(Text, nullable=True)
    description = Column(Text, nullable=True)

    def __init__(self, user_id=None, facebook=None, twitter=None, instagram=None, description=None):
        self.user_id = user_id
        self.facebook = facebook
        self.twitter = twitter
        self.instagram = instagram
        self.description = description


class TempActorModel(Base):
    __tablename__ = 'Tempactormodel'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column('user_id', Integer(), ForeignKey('Tempactors.id'))
    category_id = Column('category_id', Integer(), ForeignKey('categories.id'))

    def __init__(self, user_id=None, category_id=None):
        self.user_id = user_id
        self.category_id = category_id


class Logs(Base):
    __tablename__='logs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(Integer())
    describe = Column(Text)

    def __init__(self,ip,describe):
        self.ip = ip
        self.describe = describe


