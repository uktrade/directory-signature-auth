import http

from sigauth.middleware import SignatureCheckMiddlewareBase
from sigauth.utils import RequestSigner


SECRET = 'super secret'


class SignatureRejectionMiddleware(SignatureCheckMiddlewareBase):
    secret = SECRET


def test_signature_rejection_rejects_missing_signature(rf):
    request = rf.get('/')

    response = SignatureRejectionMiddleware().process_request(request)

    assert response.status_code == http.client.UNAUTHORIZED


def test_signature_rejection_rejects_invalid_signature(rf):

    request = rf.get('/', HTTP_X_SIGNATURE='NOT-CORRECT')

    response = SignatureRejectionMiddleware().process_request(request)

    assert response.status_code == http.client.UNAUTHORIZED


def test_signature_rejection_accepts_valid_signature(rf, settings):
    # in practive the signature is generated on the server making the request.
    # on the requesting server, it will know the shared secret
    request_signer = RequestSigner(SECRET)
    signature = request_signer.signer.generate_signature(path='/', body='')

    request = rf.get('/', HTTP_X_SIGNATURE=signature)

    response = SignatureRejectionMiddleware().process_request(request)

    assert response is None
