with open("file5.txt", "w") as f:
	f.write(input())
with open("file5.txt", "r") as f:
	a = f.readlines()[0].split(" ")
	su = 0
	for i in a:
		su += int(i)
	print("Общяя сумма - ", su)
