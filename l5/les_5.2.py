with open("file2.txt", "r") as f:
	a = f.readlines()
	for cyc in range(len(a)):
		print("Строка - ", cyc)
		print("Кол-во слов - ", len(a[cyc].split(" ")))
