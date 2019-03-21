import falcon

from models import User

from configs import SQLAlchemyConfig

SQLAlchemyConfig.make_config()

api = falcon.API()
