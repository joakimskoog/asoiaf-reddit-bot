# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f :
    license = f.read()


setup(
    name='asoiaf',
    version='0.0.1',
    description='A reddit bot that posts data from A Song of Ice And Fire',
    long_description = readme,
    author='Joakim Skoog',
    author_email='joakimskooog@gmail.com',
    url='https://github.com/joakimskoog/asoiaf-reddit-bot',
    license = license,
    packages=find_packages(exclude=('tests', 'docs'))
)