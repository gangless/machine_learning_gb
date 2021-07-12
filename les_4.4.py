a = [int(input()) for i in range(int(input()))]
b = [a[cyc] for cyc in range(len(a)) if (a[cyc] not in a[:cyc] and a[cyc] not in a[cyc + 1:])]
print(b)
