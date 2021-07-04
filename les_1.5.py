pribil = int(input())
izder = int(input())
quan_of_employ = int(input())
if pribil > izder:
    a = pribil - izder
    print("Прибыль в - ", a)
    rentab = a / pribil
    print("Рентабельность - ", rentab)

    b = a / quan_of_employ

    print("На одного - ", b)
elif izder > pribil:
    print("Издержки в - ", izder - pribil)
else:
    print("Эквивалент")






