spis = [int(input()) for i in range(int(input()))]

new_spis = [spis[cyc] for cyc in range(1, len(spis)) if spis[cyc] > spis[cyc - 1]]

print(new_spis)
