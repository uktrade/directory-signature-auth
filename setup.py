"""
Export Directory API client
"""
from setuptools import setup, find_packages


setup(
    name='sigauth',
    version='4.1.1',
    url='https://github.com/uktrade/directory-signature-auth',
    license='MIT',
    author='Department for International Trade',
    description='Signature authentication library for Export Directory.',
    packages=find_packages(exclude=["tests.*", "tests"]),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    include_package_data=True,
    install_requires=[
        'django>=1.11.22,<3.0a1',
        'djangorestframework>=3.4.7,<4.0.0',
        'mohawk>=0.3.4,<1.0.0',
    ],
    extras_require={
        'test': [
            'pytest==3.10.0',
            'pytest-cov==2.7.1',
            'pytest-django==3.5.0',
            'flake8==3.0.4',
            'wheel>=0.31.0,<1.0.0',
            'setuptools>=38.6.0,<39.0.0',
            'codecov',
            'twine',
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
