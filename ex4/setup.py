try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Parsing Arguments',
    'author': 'Orlov Yaroslav',
    'url': 'https://github.com/yarorlov/python.git',
    'download_url': 'https://github.com/yarorlov/python.git',
    'author_email': 'epoc@mail.ru',
    'version': '0.1',
    'install_requires': ['pytest'],
    'packages': ['sample'],
    'scripts': [],
    'name': 'parseargs'

}

setup(**config)