def fact(n):
	this_f = 1
	for i in range(2, n + 1):
		this_f *= i
		yield this_f
		
for el in fact(5):
	print(el)
