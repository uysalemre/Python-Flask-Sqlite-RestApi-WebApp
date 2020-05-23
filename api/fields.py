from flask_restful import fields

actor_fields = {
    'category': fields.String,
    'name': fields.String,
    'surname': fields.String,
    'gender': fields.String,
    'age': fields.Integer,
    'height': fields.Integer,
    'weight': fields.Integer,
    'bodycolor': fields.String,
    'haircolor': fields.String,
    'hairtype': fields.String,
    'eyecolor': fields.String,
    'breast': fields.Integer,
    'waist': fields.Integer,
    'hip': fields.Integer,
    'foot': fields.Integer,
    'photo1': fields.String,
    'photo2': fields.String,
    'photo3': fields.String,
    'photo4': fields.String,
    'photo5': fields.String,
    'photo6': fields.String,
    'photo7': fields.String,
    'photo8': fields.String,
    'photo9': fields.String,
    'photo10': fields.String
}

serve_fields = {
    'name': fields.String,
    'surname': fields.String
}
