"""
token生成
"""
import datetime
import functools
import jwt
from django.conf import settings


class LoginTokenGenerator(object):
    """
    Strategy object used to generate and check tokens for the password
    reset mechanism.
    """

    def __init__(self, coding=settings.ENCODEING, aud='bbx'):
        self.aud = aud
        self.payload = {
            'exp': datetime.datetime.utcnow() + settings.TOKEN_EXPIRE,
            'nbf': datetime.datetime.utcnow(),
            'iat': datetime.datetime.utcnow(),
            'aud': self.aud
        }

        self.header = {
            'typ': 'JWT',
            'alg': 'HS256'
        }

    def make_token(self, username):
        """
        返回一个jwt标准的token
        """
        self.payload['username'] = username
        return jwt.encode(self.payload, settings.LOGIN_TOKEN_SECRET, headers=self.header).decode(settings.ENCODEING)

    def check_token(self, token):
        """
        更具获取到的数据检验token有效性, 并返回数据
        """
        return jwt.decode(token.encode(settings.ENCODEING), settings.LOGIN_TOKEN_SECRET, audience=self.aud)


def need_token(aud="bbx"):
    def decorator(view_func):
        """需要token验证的装饰器"""
        @functools.wraps(view_func)
        def wrapper(request, *args, **kwargs):
            token = request.META["HTTP_TOKEN"]
            if not LoginTokenGenerator(aud).check_token(token):
                raise ValueError
            else:
                return view_func(request, *args, **kwargs)
        return wrapper
    return decorator
