with open("file6.txt", "r") as f:
	a = f.readlines()
	with_data = {}
	for i in a:
		this_proj = i.split(":")[0]
		with_data[this_proj] = 0
		b = i.split(" ")
		for i2 in b:
			c = i2.split("(")
			for i3 in c:
				try:
					with_data[this_proj] += int(i3)
				except ValueError:
					pass
print(with_data)
