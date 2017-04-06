from hashlib import sha256
from urllib.parse import urlsplit

from django.utils.crypto import constant_time_compare


class Signer:
    secret = None

    def __init__(self, secret):
        self.secret = secret

    def generate_signature(self, path, body):
        hash_object = sha256()
        if path:
            hash_object.update(ensure_bytes(path))
        if body:
            hash_object.update(ensure_bytes(body))
        hash_object.update(ensure_bytes(self.secret))
        return hash_object.hexdigest()


class RequestSigner:
    header_name = 'X-Signature'
    signer = None

    def __init__(self, secret):
        self.signer = Signer(secret)

    def get_signature_headers(self, url, body):
        path = get_path(url)
        signature = self.signer.generate_signature(path=path, body=body)
        return {
            self.header_name: signature
        }


class RequestSignatureChecker:
    header_name = 'HTTP_X_SIGNATURE'
    signer = None

    def __init__(self, secret):
        self.signer = Signer(secret)

    def test_signature(self, request):
        """
        Thest that the signature header matches the expected value.

        Args
            request (django.http.Request): The request to check the properties.
        Returns:
            bool: False if rejected, True if accepted

        """

        provided_value = request.META.get(self.header_name)

        if not provided_value:
            return False

        expected_value = self.signer.generate_signature(
            path=request.get_full_path(),
            body=request.body,
        )
        return constant_time_compare(expected_value, provided_value)


def ensure_bytes(value):
    value = value or ''
    if isinstance(value, str):
        value = bytes(value, "utf-8")
    return value


def get_path(url):
    """
    Get the path from a given url, including the querystring.

    Args:
        url (str)
    Returns:
        str

    """

    url = urlsplit(url)
    path = url.path
    if url.query:
        path += "?{}".format(url.query)
    return path
