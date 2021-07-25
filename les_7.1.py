class Matrix:
	def __init__(self, size_y):
		matrix = []
		for y_cycle in range(size_y):
			matrix.append(input().split(" "))
		self.matrix = matrix
	
	def __str__(self, x):
		
		for y_cycle in range(len(x)):
			for x_cycle in range(len(x[y_cycle])):
				print(x[y_cycle][x_cycle], end = " ")
			
			print()
	
	def __add__(self, m1, m2):
		assert len(m1) == len(m2)
		m3 = []
		for y_cycle in range(len(m1)):
			m3.append([])
			assert len(m1[y_cycle]) == len(m2[y_cycle])
			for x_cycle in range(len(m1[y_cycle])):
				m3[-1].append(int(m1[y_cycle][x_cycle]) + int(m2[y_cycle][x_cycle]))

		return m3		
				
mc = Matrix(3)	
matrix1 = mc.matrix
mc2 = Matrix(3)
matrix2 = mc2.matrix

mc.__str__(matrix1)
matrix3 = mc.__add__(matrix1, matrix2)
#print(matrix3)
#print(mc, mc.matrix)



