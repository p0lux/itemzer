import requests
from bs4 import BeautifulSoup as bs

class RequestPage:

	def __init__(self, name):
		self.name = name

	def get_content_page(self):

		request = requests.get("https://champion.gg/champion/%s" % self.name).content
		
		return request

	def return_content_bs(self):
		
		bsoup = bs(self.get_content_page(), 'html.parser')

		return bsoup
