import re

#check to see if the HEX code is real
def checkHex(hex):
	match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', hex)

	return match #if True = it is a real HEX color
#check to see if the HEX code is real

