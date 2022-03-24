""" A simple JSON to Text module to serialize JSON object.
See:
https://github.com/xrdavies/json2text
"""

from setuptools import setup, find_packages
from codecs import open
from os import path
import json2text

here = path.abspath(path.dirname(__file__))

setup(
    name='json2text',

    version=json2text.__version__,

    description='A simple JSON to Text module to serialize JSON object. Convert JSON object to text and back.',

    url='https://github.com/xrdavies/json2text',

    author='Rui Xie',
    author_email='xrdavies@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='json2text json text',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=['json2text',],

    install_requires=[
        "jsonmerge >= 1.8.0"
    ],

    # List additional groups of dependencies here
    extras_require={},
)
