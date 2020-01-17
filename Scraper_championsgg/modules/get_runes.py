from modules.request_page import RequestPage
from termcolor import colored


class GetRunes:

	def __init__(self, name):
		self.name = name

	def get_runes(self):

		list_runes = []
		
		get_runes_section = RequestPage(self.name).return_content_bs().find('section', id="primary-path")

		runes_index = 1						
		# Get title first runes
		list_runes.append(get_runes_section.find('div', class_="KeyStoneSlot__Title-krZhKQ eQgjEC Description__Title-jfHpQH bJtdXG").text)

		# Get all first runes
		for atout in get_runes_section.find_all('div', class_="Description__Title-jfHpQH bJtdXG"):
			list_runes.append(atout.text)

		second_runes = RequestPage(self.name).return_content_bs().find('section', id='secondary-path')

		# Get title second runes
		for atout2 in second_runes.find_all('div', class_="Description__Title-jfHpQH eOLOWg"):
			list_runes.append(atout2.text)

		for extra in second_runes.find_all('div', class_="Description__Title-jfHpQH bJtdXG"):
			list_runes.append(extra.text)

		return list_runes


	def list_runes(self):

		index = 1
		print(colored("=== RUNES ===", 'red'))
		for value in self.get_runes():
			print("%s : %s" % (colored(index, 'green'), colored(value, 'cyan')))
			index += 1
