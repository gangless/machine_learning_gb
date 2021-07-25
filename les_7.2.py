from abc import ABC, abstractmethod
class Cloth(ABC):
	@abstractmethod
	def make_cloth(self):
		pass

class Making(Cloth):
	def make_cloth(self, v, h, quan_palt, quan_costume):
		first = (v / 6.5 + 0.5) * quan_palt
		second = (2 * h + 0.3) * quan_costume
		all_tkan = first + second
		
		self.all_tkan = all_tkan
		
	@property	
	def print_need(self):
		return "Необходимое количество ткани - {}".format(self.all_tkan)

mc = Making()
mc.make_cloth(5, 10, 3, 2)
print(mc.print_need)

