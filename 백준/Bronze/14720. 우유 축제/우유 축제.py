how_many = int(input())
milks = list(map(int, input().split()))

count = 0
flow = [0, 1, 2]

for i in range(how_many):
    if milks[i] == flow[(count+3) % 3]:
        count += 1

print(count)