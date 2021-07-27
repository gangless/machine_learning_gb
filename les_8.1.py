class Data:
	#def __init__(self):
	stroka = input()
		
	@classmethod	
	def izv(cls):	
		this = cls.stroka
		day, mes, year = map(int, this.split(":"))
		
		return day, mes, year
		
	
	@staticmethod
	def valid(day, mes, year):
		if day < 1 or day > 31:
			print("Incorrect day")
		if mes < 1 or mes > 12:
			print("Incorrect mes")
				
		
		
#mc = Data()
day, mes, year = Data.izv()
Data.valid(day, mes, year)

		
