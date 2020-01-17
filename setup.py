#! /usr/bin/env python3
from setuptools import setup, find_packages

setup(
   name='champsgg-scraper',
   version='1.1',
   description='Module for getting informations for League of Legend champions',
   author='p0',
   author_email='kylian.p@protonmail.ch',
   packages=['scraper'],
   url="https://github.com/p0lux/Scraper_LeagueOfLegend",
   install_requires=['requests', 'beautifulsoup4', 'termcolor'],
   entry_points={"console_scripts": ["scraper=scraper.__main__:main",]}
)

