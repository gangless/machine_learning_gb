a = []
quan_of_elem = int(input())
for i in range(quan_of_elem):
    a.append(input())

new_a = a.copy()
for i in range(0, quan_of_elem - 1, 2):
    new_a[i] = a[i + 1]
    new_a[i + 1] = a[i]

print(new_a)







