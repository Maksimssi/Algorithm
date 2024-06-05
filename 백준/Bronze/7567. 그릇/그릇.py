dish = list(input())
height = 10


for i in range(len(dish)):
    last = dish.pop()
    if dish:
        if last == dish[-1]:
            height += 5
        else:
            height += 10


print(height)