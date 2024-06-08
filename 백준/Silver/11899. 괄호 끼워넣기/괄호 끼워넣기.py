gwalho = input()
open, close = 0, 0

for y in gwalho:
    if y == '(':
        open += 1
    else:
        if open != 0:
            open -= 1
        else:
            close += 1

print(open+close)