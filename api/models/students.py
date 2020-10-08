from api.utils.database import db
from marshmallow_sqlalchemy import ModelSchema
from marshmallow import fields

class Student(db.Model):
    __tablename__ = 'student'
    s_roll = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    s_class = db.Column(db.String(10))
    marks = db.Column(db.Integer)

    def __init__(self, name, s_class, marks):
        self.name = name
        self.s_class = s_class
        self.marks = marks

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

class StudentSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Student
        sqla_session = db.session

    s_roll = fields.Number(dump_only=True)
    name = fields.String(required=True)
    s_class = fields.String(required=True)
    marks = fields.Number(required=True)