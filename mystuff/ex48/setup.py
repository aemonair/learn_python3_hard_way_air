try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My ex48 Project',
    'author': 'Aemonair',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex48'],
    'scripts': [],
    'name': 'project_ex48'
}

setup(**config)
