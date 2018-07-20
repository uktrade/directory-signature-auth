from django.conf import settings

from sigauth.middleware import SignatureCheckMiddlewareBase


class TestSignatureCheckMiddleware(SignatureCheckMiddlewareBase):
    secret = settings.SIGNATURE_SECRET
