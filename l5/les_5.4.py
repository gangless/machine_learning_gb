a = ["Один", "Два", "Три", "Четыре"]
with open("file4.txt", "r") as f:
	with open("file4_2.txt", "w") as f2:
		for line in f:
			f2.writelines(str(a[int(line.split(" ")[2]) - 1]) + " - " +  line.split(" ")[2])
				
