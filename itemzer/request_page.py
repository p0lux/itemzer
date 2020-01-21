import requests
from bs4 import BeautifulSoup as bs


def return_content_bs(name):
	request = requests.get("https://champion.gg/champion/%s" % name).content
	bsoup = bs(request, 'html.parser')
	return bsoup


def return_content_op(name):
	request = requests.get('http://www.op.gg/champion/%s/statistics/top' % name).content
	bsoup = bs(request, 'html.parser')
	return bsoup


def return_content_lol_counter(name):
	request = requests.get('https://lolcounter.com/champions/%s' % name).content
	bsoup = bs(request, 'html.parser')
	return bsoup