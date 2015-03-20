import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'soundcloud_cli',
    'author': 'Giulio Calacoci',
    'url': 'https://github.com/gcalacoci/scloud_cli_utils',
    'download_url': 'https://github.com/gcalacoci/scloud_cli_utils',
    'author_email': 'asdmaster@gmail.com',
    'version': '0.1a1',
    'install_requires': ['Jinja2', 'soundcloud'],
    'packages': ['soundcloud_cli'],
    'scripts': [],
    'name': 'soundcloud_cli'
}

setup(**config)
