from scraper.request_page import RequestPage
from termcolor import colored

class GetSkills:

	def __init__(self, name):
		self.name = name

	def get_skills(self):
		
		counter_skills = 1
		get = RequestPage(self.name).return_content_op().find('table', class_='champion-skill-build__table')
		get_table = get.find_all('td')
		list_skills = [value.text.replace('\t', '').replace('\n', '') for value in get_table]
		

		print(colored("=== FIRST 3 SKILLS === ", 'green'))
		print(" ".join(list_skills[:3]))
		
		