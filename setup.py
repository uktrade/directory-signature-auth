"""
Export Directory API client
"""
from setuptools import setup, find_packages


setup(
    name='sigauth',
    version='5.1.2',
    url='https://github.com/uktrade/directory-signature-auth',
    license='MIT',
    author='Department for International Trade',
    description='Signature authentication library for Export Directory.',
    packages=find_packages(exclude=["tests.*", "tests"]),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    include_package_data=True,
    install_requires=[
        'django>=3.2.18,<4.0.0',
        'djangorestframework>=3.4.7,<4.0.0',
        'mohawk>=0.3.4,<2.0.0',
    ],
    extras_require={
        'test': [
            'pytest==6.1.0',
            'pytest-cov==2.10.1',
            'pytest-django==3.10.0',
            'flake8==3.8.3',
            'wheel>=0.31.0,<1.0.0',
            'setuptools>=38.6.0,<39.0.0',
            'codecov',
            'twine',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3.9",
)
