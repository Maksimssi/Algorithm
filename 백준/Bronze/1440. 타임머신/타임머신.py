si, bun, cho = map(int,input().split(':'))

time = 0

for i in si,bun,cho:
    if 1 <= i <= 12:
        time += 2
    elif i > 59:
        time = 0
        break

print(time)