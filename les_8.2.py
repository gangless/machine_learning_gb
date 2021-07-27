class MyExcep(Exception):
	def __init__(self, fir):
		print(fir / 1)
	
a, b = map(int, input("Введите два числа для деления через пробел\n").split(" "))
if not b:
	try:
		raise MyExcep(a)
	except MyExcep:
		pass
else:
	print(a / b)

	
	
