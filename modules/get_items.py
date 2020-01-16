from modules.request_page import RequestPage
from termcolor import colored


class GetItems:

	def __init__(self, name):
		self.name = name

	def get_items(self):

		list_items = []
		
		items = RequestPage(self.name).return_content_bs().find("div", class_="build-wrapper")

		for lien in items.find_all('a', href=True):
			list_items.append(lien['href'].split('/')[-1])

		item_index = 1

		print(colored("=== ITEMS ===", "red"))

		for value_item in list_items:
			print("%s : %s" % (colored(item_index, "green"), colored(value_item, 'cyan')))
			item_index += 1
