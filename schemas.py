from marshmallow_sqlalchemy import ModelSchema

from models import User, Post


class UserSchema(ModelSchema):
    class Meta:
        model = User


class PostSchema(ModelSchema):
    class Meta:
        model = Post


user_schema = UserSchema()
users_schema = UserSchema(many=True)
post_schema = PostSchema()
posts_schema = PostSchema(many=True)
