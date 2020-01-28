def likes(names):
	if len(names) <= 1:
		return ''.join("{} likes this".format(names[0]) if names else "no one likes this")
	elif len(names) == 2:
		return ''.join("{0} and {1} like this".format(names[0], names[1]))
	elif len(names) == 3:
		return ''.join("{0}, {1} and {2} like this".format(names[0], names[1], names[2]))
	else:
		return ''.join("{0}, {1} and {2} others like this".format(names[0], names[1], len(names) - 2))
	# if names:
	# 	if len(names) == 1:
	# 		return ''.join(names[0] + " likes this")
	# 	elif len(names) == 2:
	# 		return ''.join(names[0] + " and " + names[1] + " like this")
	# 	elif len(names) == 3:
	# 		return ''.join(names[0] + ", " + names[1] + " and " + names[2] + " like this")
	# 	else:
	# 		return ''.join(names[0] + ", " + names[1] + " and " + str(len(names) - 2) + " others like this")
	# else:
	# 	return "no one likes this"	



if __name__ == '__main__':
    names = []
    print likes(names)

# likes [] // must be "no one likes this" - OK
# likes ["Peter"] // must be "Peter likes this" -OK
# likes ["Jacob", "Alex"] // must be "Jacob and Alex like this" - OK
# likes ['Max', 'John', 'Mark']), 'Max, John and Mark like this') - OK
# likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this" - OK