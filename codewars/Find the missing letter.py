def unique(s):
	# return [x for x in list(map(chr, range(97, 123))) if x in s]
	# b = list(map(chr, range(97, 123)))
	# return [i for i in b + s if i not in b or i not in s]
	return chr(list(set(range(ord(s[0]), ord(s[-1]) + 1)).difference([ord(x) for x in s]))[0])
	# [ord(x) for x in s]
	# 	print ord(x) # chr(97)

if __name__ == '__main__':
    print unique(["a","b","c","d","f"]) # e
    print unique(["r","s","u","v","w"]) # t
    print unique(["O","Q","R","S"])