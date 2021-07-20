class Worker:
	def __init__(self, name, surname, position, _income):
		self.name = name
		self.surname = surname
		self.position = position
		self._income = _income
	
class Position(Worker):
	def get_full_name(self):
		print("{} {}".format(self.name, self.surname))
	
	def get_total_income(self):	
		print("Общий - ", self._income["wage"] + self._income["bonus"])
a = Position("A", "B", 1, {"wage": 500, "bonus": 0})
a.get_full_name()	
a.get_total_income()
