from setuptools import setup, find_packages

setup(
    name='jobsitychat',
    version='0.1',
    py_modules=['jobsitychat'],
    install_requires=[
        'simplejson',
        'boto3',
        'pandas',
        'peewee',
        'pylint',
        'pytest',
        'pytest-cov',
        'pytest-mock',
        'pytest-watch',
        'pycryptodome',
        'mock',
        'baseconvert'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
