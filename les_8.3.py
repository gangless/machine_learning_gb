
b = []

while True:
	a = input()
	
	if a == "stop":
		break
	
	try:
		c = float(a)
		b.append(a)
	except ValueError:
		print("Введено не число")
	
print(b)	
