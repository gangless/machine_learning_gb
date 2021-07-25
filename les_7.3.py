class Kletka:
	def __init__(self, quan):
		self.quan = quan
	
	def __add__(self, other):
		new_quan = self.quan + other.quan
		return new_quan
		
	def __sub__(self, other):
		if self.quan == other.quan:
			print("Вычитание невозможно")
			return None
		else:
			new_quan = abs(self.quan - other.quan)
			return new_quan
	
	def __mul__(self, other):
		new_quan = self.quan * other.quan
		return new_quan
		
	def __truediv__(self, other):
		if self.quan >= other.quan:
			new_quan = self.quan // other.quan
		else:
			new_quan = other.quan // self.quan
		return new_quan
		
	
	def make_order(self, riad):
		qq = self.quan // riad
		for i in range(qq):
			print("".join(["*" for s in range(riad)]))
		last = self.quan - (qq * riad)
		
		print("".join(["*" for s in range(last)]), end="")


mc1 = Kletka(15)
mc2 = Kletka(10)

new1 = (mc1 + mc2)
new2 = (mc1 - mc2)
new3 = (mc1 * mc2)
new4 = (mc1 / mc2)

mc3 = Kletka(new1)
mc3.make_order(5)
	
	
