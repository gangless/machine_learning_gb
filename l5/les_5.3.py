with open("file3.txt", "r") as f:
	sred = 0
	quan = 0
	for line in f:
		name, doxod = line.split(" ")
		if int(doxod) < 20000:
			print(name)
		sred += int(doxod)
		quan += 1
	print("Среднее - ", sred / quan)
