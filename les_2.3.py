a = int(input())

dict_with_all = {"Зима": [12, 1, 2], "Весна": [3, 4, 5], "Лето": [6, 7, 8], "Осень": [9, 10, 11]}

for key, value in dict_with_all.items():
    if a in value:
        print(key)
        break
