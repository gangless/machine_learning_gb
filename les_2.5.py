

n = int(input())
a = []
a.append(int(input()))
for i in range(1, n):
    new_value = int(input())
    for i2 in range(len(a)):
        if new_value >= a[i2]:
            a.insert(i2, new_value)
            break

        elif i2 == len(a) - 1:
            a.append(new_value)


    print(a)


