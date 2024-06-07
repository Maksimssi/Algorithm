dwarfs = [int(input()) for _ in range(9)]

dwarfs.sort()
over = sum(dwarfs) - 100
eight = 0
nine = 0

for i in range(9):
    for j in range(i+1,9):
        if dwarfs[i]+dwarfs[j]==over:
            eight, nine = dwarfs[i], dwarfs[j]
dwarfs.remove(eight)
dwarfs.remove(nine)

for dwarf in dwarfs:
    print(dwarf)