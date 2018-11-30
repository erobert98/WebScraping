import re


def parse_names(bad_names):
	names = []
	for name in bad_names:				#takes care of converting selenium objects to text
		names.append(name.text)

	previous_names = []   #initialize our list of names
	regex = r"ed (.*)"  	# our regex
	for name in names:  	
		matches = re.findall(regex, name, re.MULTILINE)
		for match in matches:
			previous_names.append(match)
			print(match)
	test = ' and '.join(previous_names)
	return test



if __name__ == '__main__':
	pass
	# var = ["Previously named PB’s Sydney Australia\n", "Previously named Proud Boys Sydney Australia"]
	# parse_names(var)