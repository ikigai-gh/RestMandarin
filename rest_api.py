import falcon

from resources import UsersResource, UserResource, PostsResource, PostResource

from configs import SQLAlchemyConfig

SQLAlchemyConfig.make_config()

api = falcon.API()

api.add_route('/users/', UsersResource())
api.add_route('/users/{user_id}/', UserResource())
api.add_route('/users/{user_id}/posts/', PostsResource())
api.add_route('/users/{user_id}/posts/{post_id}/', PostResource())
