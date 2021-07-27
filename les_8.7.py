class Operation:
	#5+3i
	def __add__(a, b):
		fir1, sec1 = map(int, a.replace("i", "").split("+"))
		fir2, sec2 = map(int, b.replace("i", "").split("+"))
		
		s1 = sec1 + sec2
		if s1 >= 0:
			new = str(fir1 + fir2) + "+" + str(s1) + "i"
		else:
			new = str(fir1 + fir2) + "-" + str(s1) + "i"
		
		return new
		
	def __mul__(a, b):
		fir1, sec1 = map(int, a.replace("i", "").split("+"))
		fir2, sec2 = map(int, b.replace("i", "").split("+"))
		
		s1 = fir1 * sec2 + fir2 * sec1
		if s1 >= 0:
			new = str(fir1 * fir2 - sec1 * sec2) + "+" + str(s1) + "i"
		else:
			new = str(fir1 * fir2 - sec1 * sec2) + "-" + str(s1) + "i"
		return new
	


c1 = Operation.__add__("5+3i", "12+4i")
c2 = Operation.__mul__("5+3i", "12+4i")
print(c1)
print(c2)
	
