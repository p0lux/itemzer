 #! /usr/bin/env python3 

# import scraper

from scraper.get_items import GetItems
from scraper.get_runes import GetRunes

import sys   

def main():
        
    GetItems(sys.argv[1]).get_items()
    GetRunes(sys.argv[1]).list_runes()
    #GetSkills(sys.argv[1]). 

if __name__ == "__main__":
    main()

		

