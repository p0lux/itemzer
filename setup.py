#! /usr/bin/env python3
from setuptools import setup

setup(
   name='Scraper_championsgg',
   version='1.0',
   description='Module for getting informations for League of Legend champions',
   author='p0',
   author_email='kylian.p@protonmail.ch',
   packages=['Scraper_championsgg'], 
   install_requires=['requests', 'beautifulsoup4', 'termcolor'],
   scripts=[
   			'modules/get_items',
   			'modules/get_runes'
   			]
)

