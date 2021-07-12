
def f_plus(a, value):
	value += sum([int(cyc) for cyc in a])
	return value

value = 0
while True:
	b = input().split(" ")
	if "_" == b[0]:
		break
	elif "_" in b:
		b = b[0:b.index("_")]
		value = f_plus(b, value)
		print(value)
		break
	else:
		value = f_plus(b, value)
		print(value)
	
