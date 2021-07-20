class Road:
	def __init__(self, _length, _width, _mass, _sm):
		formula = _length * _width * _mass * _sm
		print(formula / 1000, "т")

a = Road(20, 5000, 25, 5)


