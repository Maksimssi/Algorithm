import sys

num = int(sys.stdin.readline())
list = []

for i in range(num):
    list.append(sys.stdin.readline().rstrip())

for i in range(num):
    list2 = list[i].split()
    print(f'Case #{i+1}: ',end='')
    for _ in range(len(list2)):
        print(list2.pop() + ' ',end='')
    print()