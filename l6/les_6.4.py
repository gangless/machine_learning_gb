class Car:
	def __init__(self, speed, color, name, is_police):
		self.color = color
		self.speed = speed
		self.name = name
		self.is_police = is_police
		
	def go(self):
		print("Машина поехала")
	
	def stop(self):
		print("Машина остановилась")
		
	def turn(self, direction):
		print("Маишна повернула - ", direction)
	
	def show_speed(self):
		print("Текущая скорость - ", self.speed)
	

class TownCar(Car):
	def show_speed(self):
		if self.speed > 60:
			print("Превышение скорости")
		else:
			print("Текущая скорость - ", self.speed)
			
class SportCar(Car):
	pass
	
class WorkCar(Car):
	def show_speed(self):
		if self.speed > 40:
			print("Превышение скорости")
	
class PoliceCar(Car):
	pass

a1 = TownCar(62, "r", "TT", False)
a1.go()

a1.stop()

a1.turn("Право")

a1.show_speed()
	
