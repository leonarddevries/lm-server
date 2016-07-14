# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from os.path import join, dirname
version = {}
with open(join(dirname(__file__), "lightmanager", "server", "version.py")) as fp:
    exec (fp.read(), version)
with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
    name='lm-localclient',
    version=version['__version__'],
    packages=find_packages(exclude=('tests', 'docs')),
    url='https://github.com/leonarddevries/lm-localclient',
    license='MIT',
    author='Leonard de Vries',
    author_email='leonard@ldvengineering.nl',
    description='Remote control and monitor of one or more local light manager instances',
    install_requires=required,
)
