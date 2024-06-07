import sys

count = int(input())

tickets = list(map(int,sys.stdin.readline().split()))

tickets.sort(reverse=True)

num = 1
while True:
    if num > count:
        print(num)
        break
    else:
        if num == tickets[-1]:
            tickets.pop()
            num += 1
        else:
            print(num)
            break