from itertools import count
from itertools import cycle
def number_more(numb):
	# Числа в 10 раз больше
	for i in count(numb):
		if i > numb * 4:
			break
		else:
			print(i)
	
b = [1, 2, 3, 4]	
c = 0
for el in cycle(b):
	if c > len(b) * 5:
		break
	print(el)
	c += 1
