from sigauth import helpers


SECRET = 'super-duper-secret'


def test_signer_without_body():
    signer = helpers.RequestSigner(secret=SECRET, sender_id='test')

    headers = signer.get_signature_headers(
        url='http://e.co/',
        body='',
        method='POST',
        content_type='application/json'
    )

    assert 'id="test' in headers[signer.header_name]


def test_signer_with_body():
    signer = helpers.RequestSigner(secret=SECRET, sender_id='test')

    headers = signer.get_signature_headers(
        url='http://e.co/',
        body='content',
        method='POST',
        content_type='application/json'
    )

    assert 'id="test' in headers[signer.header_name]


def test_request_signer_passes_correct_secret_to_signer(settings):
    signer = helpers.RequestSigner(secret=SECRET, sender_id='test')

    assert signer.secret == SECRET


def test_get_path_with_querystring():
    assert helpers.get_path('http://e.co/?thing=1') == '/?thing=1'


def test_get_path_without_querystring():
    assert helpers.get_path('http://e.co/aa/') == '/aa/'


def test_signer_authorisation():
    signer = helpers.RequestAuthorisationSigner(secret=SECRET, sender_id='test')

    headers = signer.get_signature_headers(
        url='http://e.co/',
        body='content',
        method='POST',
        content_type='application/json'
    )

    assert signer.secret == SECRET
    assert signer.sender_id == 'test'
    assert 'id="test' in headers[signer.header_name]
