from flask.ext.restful import Api, abort
from flask.ext.restful.representations.json import settings as json_settings

from flask.ext.jwt import JWT, jwt_required
from flask.ext.cors import CORS

from webargs.flaskparser import parser

from clapperboard.resources.movie import (
    MovieAPI,
    MovieListAPI,
    MovieIMDBDataAPI,
    MovieMetaDataAPI,
    MovieShowTimesListAPI,
    MovieShowTimeAPI
)
from clapperboard.resources.showtime import ShowTimeAPI, ShowTimesListAPI
from clapperboard.resources.theatre import TheatreAPI, TheatreListAPI
from clapperboard.resources.technology import TechnologyAPI, TechnologyListAPI
from clapperboard.resources.user import (
    UserAPI,
    UserListAPI,
    UserVerifyEmailAPI,
    UserResendVerificationEmail
)
from clapperboard.models.user import User


class ClapApi(Api):
    def make_response(self, data, *args, **kwargs):
        # TODO: This is unreliable!
        if locals()['args'][0] >= 400:
            if isinstance(data['status'], int):
                data['code'] = data['status']
            data['status'] = "error"
        return super(ClapApi, self).make_response(data, *args, **kwargs)


api = ClapApi(decorators=[jwt_required()])
anon_api = ClapApi()
jwt = JWT()
cors = CORS()


api.add_resource(MovieListAPI, '/movies')
api.add_resource(MovieAPI, '/movies/<int:movie_id>')
api.add_resource(MovieIMDBDataAPI, '/movies/<int:movie_id>/imdb-data')
api.add_resource(MovieMetaDataAPI, '/movies/<int:movie_id>/metadata')
api.add_resource(MovieShowTimesListAPI, '/movies/<int:movie_id>/showtimes')
api.add_resource(
    MovieShowTimeAPI, '/movies/<int:movie_id>/showtimes/<int:showtime_id>'
)

api.add_resource(ShowTimesListAPI, '/showtimes')
api.add_resource(ShowTimeAPI, '/showtimes/<int:showtime_id>')

api.add_resource(TheatreListAPI, '/theatres', '/theatres/')
api.add_resource(TheatreAPI, '/theatres/<int:theatre_id>')

api.add_resource(TechnologyListAPI, '/technologies')
api.add_resource(TechnologyAPI, '/technologies/<int:technology_id>')

anon_api.add_resource(UserListAPI, '/users')
api.add_resource(UserAPI, '/users/<int:user_id>')
anon_api.add_resource(
    UserVerifyEmailAPI, '/users/verify-email/<string:payload>'
)
api.add_resource(
    UserResendVerificationEmail,
    '/users/<int:user_id>/resend-email-verification'
)


def user_verify_email_url(payload):
    return anon_api.url_for(
        UserVerifyEmailAPI,
        payload=payload,
        _external=True
    )


json_settings['indent'] = 4


@parser.error_handler
def webargs_error_handler(err):
    """
    webargs error handler that uses Flask-RESTful's abort function to return
    a JSON error response to the client.
    """
    code, msg = (
        getattr(err, 'status_code', 400),
        getattr(err, 'message', 'Invalid Request')
    )
    abort(code, status='error', code=code, message=msg)


@jwt.authentication_handler
def authenticate(username, password):
    u = User.query.filter_by(username=username).first()
    if u and u.check_password(password):
        return u


@jwt.user_handler
def load_user(payload):
    return User.query.get(payload['user_id'])
