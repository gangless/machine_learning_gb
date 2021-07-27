def check(dan):
	if isinstance(dan, type(1)):
		return True
	else:
		print("Неккоректно введены данные")
		return False

class Sklad:
	kol_vo = 0
	different_sklad = {}
	def plus(self, param):
		if check(param):
			self.kol_vo += param
		
	def priem(self, param, kuda):	
		if check(param):
			if kuda not in self.different_sklad.keys():
				self.different_sklad[kuda] = param
			else:
				self.different_sklad[kuda] += param
	
	def print_sklad(self):
		print(self.different_sklad)

class Tech_all(Sklad):
	def just_print(self):
		print("Общий класс")

		
class Printer(Tech_all):		
	quan = 0
	def __init__(self):
		print("Принтер")

	def plus_print(self, param):		
		if check(param):
			self.quan += param
			
	def printe(self):
		print(self.quan)


class Skaner(Tech_all):
	quan = 0
	def __init__(self):
		print("Сканер")
		
	def plus_skaner(self, param):
		if check(param):
			self.quan += param			


	def printe(self):
		print(self.quan)
	
mc = Sklad()


mc.priem(12, "Amsterdam")
mc.print_sklad()

mc.priem("sss", "aaaa")

