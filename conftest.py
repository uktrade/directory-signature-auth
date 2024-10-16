def pytest_configure():
    from django.conf import settings
    settings.configure(
        ROOT_URLCONF='tests.urls',
        SIGAUTH_URL_NAMES_WHITELIST=['url-one'],
        SIGAUTH_NAMESPACE_WHITELIST=['blah'],
        MIDDLEWARE=['tests.middleware.TestSignatureCheckMiddleware'],
        SIGNATURE_SECRET='super secret',
        SECRET_KEY='test-key',
    )
