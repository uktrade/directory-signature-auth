def pytest_configure():
    from django.conf import settings
    settings.configure(
        ROOT_URLCONF='tests.urls',
        SIGAUTH_URL_NAMES_WHITELIST=['url-one'],
        MIDDLEWARE_CLASSES=['tests.middleware.TestSignatureCheckMiddleware'],
        SIGNATURE_SECRET='super secret',
    )
