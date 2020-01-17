 #! /usr/bin/env python3 

from modules.get_runes import GetRunes
from modules.get_items import GetItems

import sys   

GetItems(sys.argv[1]).get_items()
GetRunes(sys.argv[1]).list_runes()
#GetSkills(sys.argv[1]). 

		

