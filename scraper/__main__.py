 #! /usr/bin/env python3 

from scraper.get_items import GetItems
from scraper.get_runes import GetRunes
from scraper.get_skills_order import GetSkills

import sys   
import os


# Determine the OS 
# if os.name == "nt":
#     # Deactivate the color
#     pass
# else: 
#     # Activate the color
#     pass



def main():
    GetItems(sys.argv[1]).get_items()
    GetRunes(sys.argv[1]).list_runes()
    GetSkills(sys.argv[1]).get_skills() 

if __name__ == "__main__":
    main()

		

