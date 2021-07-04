n = input()
max1 = 0
i = 0
while i < len(n):
    if max1 < int(n[i]):
        max1 = int(n[i])

    i += 1

print(max1)