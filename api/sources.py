from flask_restful import Resource, reqparse, abort, marshal_with
from api.fields import actor_fields, serve_fields
from models import *
from flask_security import login_required, roles_accepted


class ActorsListApi(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str)
        self.reqparse.add_argument('surname', type=str)
        self.reqparse.add_argument('hashed', type=str)

    @login_required
    @roles_accepted('Admin', 'Guest')
    @marshal_with(serve_fields)
    def get(self):
        mockData = []
        ids = ActorModel.query.all()
        if not ids:
            abort(404, message="There is no available actor data")
        for id in ids:
            model_data = Actors.query.filter_by(id=id.user_id).first()
            temp_fields = {
                'name': model_data.name,
                'surname': model_data.surname,
            }
            mockData.append(temp_fields)
        return mockData

    @login_required
    @roles_accepted('Admin', 'Guest')
    @marshal_with(actor_fields)
    def post(self):
        parsed = self.reqparse.parse_args()
        mockData = []
        actor = Actors.query.filter_by(name=parsed['name'], surname=parsed['surname']).first()
        category_data = Categories.query.filter_by(id=actor.id).first()
        photo_data = Photos.query.filter_by(user_id=actor.id).first()
        body_data = ActorBody.query.filter_by(user_id=actor.id).first()
        temp_fields = {
            'category': category_data.name,
            'name': actor.name,
            'surname': actor.surname,
            'gender': actor.gender,
            'age': actor.age,
            'height': body_data.height,
            'weight': body_data.weight,
            'bodycolor': body_data.bodycolor,
            'haircolor': body_data.haircolor,
            'hairtype': body_data.hairtype,
            'eyecolor': body_data.eyecolor,
            'breast': body_data.top,
            'waist': body_data.middle,
            'hip': body_data.bottom,
            'foot': body_data.foot,
            'photo1': "http://static/images/model/" + photo_data.photo1 + "",
            'photo2': "http://static/images/model/" + photo_data.photo2 + "",
            'photo3': "http://static/images/model/" + photo_data.photo3 + "",
            'photo4': "http://static/images/model/" + photo_data.photo4 + "",
            'photo5': "http://static/images/model/" + photo_data.photo5 + "",
            'photo6': "http://static/images/model/" + photo_data.photo6 + "",
            'photo7': "http://static/images/model/" + photo_data.photo7 + "",
            'photo8': "http://static/images/model/" + photo_data.photo8 + "",
            'photo9': "http://static/images/model/" + photo_data.photo9 + "",
            'photo10': "http://static/images/model/" + photo_data.photo10 + ""
        }
        mockData.append(temp_fields)
        return mockData
