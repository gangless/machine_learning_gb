import json
with open("file7.txt", "r") as f:
	slovar_with_all = {}
	sred = 0
	quan = 0
	
	for line in f:
		line = line.replace(".", "").replace("\n", "").split(" ")
		pribil = int(line[2]) - int(line[3])
		if pribil >= 0:
			sred += pribil
			quan += 1
		
		slovar_with_all[line[0]] = pribil
new_spisok = [slovar_with_all, {"Average_profit": round(sred / quan, 3)}]
		
with open("file7_2.json", "w") as f:
	json.dump(new_spisok, f)		
