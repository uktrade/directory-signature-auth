from django.test import TestCase, override_settings, RequestFactory

from sigauth.middleware import SignatureRejectionMiddleware
from sigauth.utils import SignatureRejection
from sigauth.tests.client import SignatureTestClient


class BaseSignatureTestCase(TestCase):
    """
    Base TestCase providing a mock request and appropriate signature
    """

    def setUp(self):
        self.request = RequestFactory().get('/path')
        self.request._body = b'lol'
        # signature generated from the key in settings, and above path & body
        self.sig = (
            'b24d2898bf932db0f2af1e956d3596743b35cf93d7a23e699cc85eda34dd5ce2'
        )


class SignatureRejectionMiddlewareTestCase(BaseSignatureTestCase):

    def setUp(self):
        super().setUp()
        self.middleware = SignatureRejectionMiddleware()

    def test_generate_signature(self):
        signature = SignatureRejection.generate_signature(
            'secret',
            'path',
            b'body',
        )
        self.assertEqual(
            signature,
            'c6be1984f8b516e94d7257031cc47ed9863a433e461ac0117214b1b6a7801991',
        )

    @override_settings(PROXY_SIGNATURE_SECRET=SignatureTestClient.SECRET)
    def test_test_signature_missing(self):
        self.assertFalse(SignatureRejection.test_signature(self.request))

    @override_settings(PROXY_SIGNATURE_SECRET=SignatureTestClient.SECRET)
    def test_test_signature_incorrect(self):
        self.request.META['HTTP_X_PROXY_SIGNATURE'] = 'bad-signature'
        self.assertFalse(SignatureRejection.test_signature(self.request))

    @override_settings(PROXY_SIGNATURE_SECRET=SignatureTestClient.SECRET)
    def test_test_signature_correct(self):
        self.request.META['HTTP_X_PROXY_SIGNATURE'] = self.sig
        self.assertTrue(SignatureRejection.test_signature(self.request))

    @override_settings(PROXY_SIGNATURE_SECRET=SignatureTestClient.SECRET)
    def test_process_request_pass(self):
        self.request.META['HTTP_X_PROXY_SIGNATURE'] = self.sig
        self.assertEqual(self.middleware.process_request(self.request), None)

    def test_process_request_fail(self):
        response = self.middleware.process_request(self.request)
        self.assertEqual(response.status_code, 401)
