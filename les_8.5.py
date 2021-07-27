class Sklad:
	kol_vo = 0
	different_skald = {}
	def plus(self, param):
		self.kol_vo += param
		
	def priem(self, param, kuda):	
		if kuda not in self.different_sklad.keys():
			self.different_sklad[kuda] = param
		else:
			self.different_sklad[kuda] += param
		
		

class Tech_all(Sklad):
	def just_print(self):
		print("Общий класс")

		

class Printer(Tech_all):		
	quan = 0
	def __init__(self):
		print("Принтер")

	def plus_print(self, param):		
		self.quan += param

	def printe(self):
		print(self.quan)

class Skaner(Tech_all):
	quan = 0
	def __init__(self):
		print("Сканер")
		
	def plus_skaner(self, param):
		self.quan += param			
	
	def printe(self):
		print(self.quan)
	
mc = Sklad()

