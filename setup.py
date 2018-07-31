"""
Export Directory API client
"""
from setuptools import setup, find_packages


setup(
    name='sigauth',
    version='4.0.1',
    url='https://github.com/uktrade/directory-signature-auth',
    license='MIT',
    author='Department for International Trade',
    description='Signature authentication library for Export Directory.',
    packages=find_packages(exclude=["tests.*", "tests"]),
    long_description=open('README.md').read(),
    include_package_data=True,
    install_requires=[
        'django>=1.9,<2.0a1',
        'djangorestframework>=3.4.7,<4.0.0',
        'mohawk>=0.3.4,<1.0.0',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
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
