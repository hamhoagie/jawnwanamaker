from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='jawnwanamaker',
    version='0.1.0',
    description='flask project for jawnwanamaker webapp', 
    url='https://github.com/hamhoagie/jawnwanamaker',
    author='billy mcdermott',
    author_email='billy@billymcdermott.com',
    packages=find_packages(where='src'),
    install_requires=['Flask', 'Pillow', 'numpy'],
    project_urls={'Project Home': 'jawnwanamaker.com'},
)