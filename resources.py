import falcon
from falcon import HTTPConflict
from sqlalchemy.exc import IntegrityError

from configs import SQLAlchemyConfig as db
from models import User
from schemas import users_schema, user_schema
from filters import parse_filters


class UserResource:
    def on_get(self, req, resp):
        data_offset = req.params.get('offset') or 0
        limit = db.SESSION.query(User).count() / 10
        filters = parse_filters(cls_model=User, req_params=req.params)

        users = db.SESSION.query(User).filter(*filters).limit(limit).offset(data_offset)
        resp.media = users_schema.dump(users).data

    def on_post(self, req, resp):
        json = req.media
        new_user = user_schema.load(json, session=db.SESSION).data
        try:
            db.SESSION.add(new_user)
            db.SESSION.commit()
        except IntegrityError:
            raise HTTPConflict('Unique contraint failed')
        resp.status = falcon.HTTP_201
