firstrun = True

def onenter(variables, inventory, items):
	""" List items? """
	global firstrun
	print "New room?!?" if firstrun else "You have been here before. At least you think so."
	firstrun = False

	print variables, inventory, items
	return variables, inventory, items
def oncommand(command, variables, inventory, items):
	""" Process command """
	print "command:", command
	return False, variables, inventory, items
