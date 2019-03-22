import falcon

from resources import UsersResource, UserResource, PostsResource

from configs import SQLAlchemyConfig

SQLAlchemyConfig.make_config()

api = falcon.API()

api.add_route('/users/', UsersResource())
api.add_route('/users/{id}/', UserResource())
api.add_route('/users/{id}/posts/', PostsResource())