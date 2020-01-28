def maskify(cc):
	return (len(cc)-4)*"#" + cc[-4:]
    # maskify = (lambda cc:('#'*(len(cc)-4)+cc[-4:]))
    
	# if len(cc) > 4:
	# 	for x in cc[:-4]:
	# 		cc = cc.replace(x, "#", 1)
	# 	return cc	
	# else:
	# 	return cc

line = "dfghjklkjhgfghjkh7654"
print maskify(line)