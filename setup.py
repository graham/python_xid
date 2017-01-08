# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
long_description = "see https://github.com/graham/python_xid for more info."

setup(
    name='xid',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='1.0.3',

    description='Python Xid Implementation',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/graham/python_xid',

    # Author details
    author='Graham Abbott',
    author_email='graham.abbott@gmail.com',

    # Choose your license
    license='MIT',

    py_modules=['xid'],
    download_url="https://github.com/graham/python_xid/tarball/0.1",
)
