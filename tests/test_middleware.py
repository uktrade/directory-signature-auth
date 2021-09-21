from django.urls import reverse
import pytest
from sigauth.helpers import RequestSigner, RequestAuthorisationSigner
from rest_framework.exceptions import AuthenticationFailed


def test_signature_rejection_rejects_missing_signature(client):
    with pytest.raises(AuthenticationFailed):
        response = client.get(reverse('url-two'))
        assert response.status_code == 401


def test_signature_rejection_rejects_invalid_signature(client):
    with pytest.raises(AuthenticationFailed):
        response = client.get(
            reverse('url-two'), HTTP_X_SIGNATURE='hawk INCORRECT', CONTENT_TYPE=''
        )
        assert response.status_code == 401


def test_signature_rejection_accepts_valid_signature(client, settings):
    # in practive the signature is generated on the server making the request.
    # on the requesting server, it will know the shared secret
    signer = RequestSigner(secret=settings.SIGNATURE_SECRET, sender_id='test')

    headers = signer.get_signature_headers(
        url=reverse('url-two'),
        body='',
        method='GET',
        content_type=''
    )

    response = client.get(
        reverse('url-two'),
        HTTP_X_SIGNATURE=headers[signer.header_name],
        CONTENT_TYPE='',
    )

    assert response.status_code == 200


def test_signature_rejection_accepts_valid_authorisation(client, settings):
    # in practice the signature is generated on the server making the request.
    # on the requesting server, it will know the shared secret
    signer = RequestAuthorisationSigner(secret=settings.SIGNATURE_SECRET, sender_id='test')

    headers = signer.get_signature_headers(
        url='http://testserver' + reverse('url-two'),
        body='',
        method='GET',
        content_type=''
    )

    response = client.get(
        reverse('url-two'),
        data='',
        HTTP_AUTHORIZATION=headers[signer.header_name],
        CONTENT_TYPE='',
    )

    assert response.status_code == 200


def test_signature_rejection_accepts_in_valid_raise_exceptiom(client, settings):
    # in practice the signature is generated on the server making the request.
    # on the requesting server, it will know the shared secret
    signer = RequestAuthorisationSigner(secret='incorrect', sender_id='test2')

    headers = signer.get_signature_headers(
        url='http://testserver' + reverse('url-two'),
        body='',
        method='GET',
        content_type=''
    )
    with pytest.raises(AuthenticationFailed):
        response = client.get(
            reverse('url-two'),
            data='',
            HTTP_AUTHORIZATION=headers[signer.header_name],
            CONTENT_TYPE='',
        )

        assert response.status_code == 403


def test_signature_check_skipped(client):
    response = client.get(reverse('url-one'))

    assert response.status_code == 200


def test_signature_check_not_skipped(client, settings):
    with pytest.raises(AuthenticationFailed):
        response = client.get(reverse('url-two'))
        assert response.status_code == 401


def test_404(client, settings):
    response = client.get('/foo')

    assert response.status_code == 404
