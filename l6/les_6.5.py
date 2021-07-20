class Stationery:
	def __init__(self, title):
		self.title = title
	
	def draw(self):
		print("запуск отрисовки")

class Pen(Stationery):
	def draw(self):
		print("Зачем создавать дочерние классы, если единственным методом у родительского не пользуемся?")	
	
class Pencil(Stationery):
	def draw(self):
		print("a")
	
class Handle(Stationery):
	def draw(self):
		print("b")	

a = Pen("ffff")
a.draw()	
