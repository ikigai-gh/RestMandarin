import falcon

from resources import UserResource

from configs import SQLAlchemyConfig

SQLAlchemyConfig.make_config()

api = falcon.API()

api.add_route('/users/', UserResource())