from sigauth import utils


SECRET = 'super-duper-secret'


def test_signer():
    signer = utils.Signer(SECRET)

    signature = signer.generate_signature('/', '')

    assert signature == (
        '7d219ea98ca799140bf8bdb13af042e84b0c5c389d00a954fe00d8790a3c8f31'
    )


def test_request_signer_passes_correct_secret_to_signer(settings):
    assert utils.RequestSigner(SECRET).signer.secret == SECRET


def test_request_signer_uses_correct_header_name(settings):
    request_signer = utils.RequestSigner(SECRET)
    headers = request_signer.get_signature_headers(
        url='http://e.co/', body=''
    )

    assert headers[request_signer.header_name] == (
        '7d219ea98ca799140bf8bdb13af042e84b0c5c389d00a954fe00d8790a3c8f31'
    )


def test_get_path_with_querystring():
    assert utils.get_path('http://e.co/?thing=1') == '/?thing=1'


def test_get_path_without_querystring():
    assert utils.get_path('http://e.co/aa/') == '/aa/'
