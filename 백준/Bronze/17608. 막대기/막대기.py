import sys

num = int(sys.stdin.readline())
list = []

for i in range(num):
    list.append(int(sys.stdin.readline()))

a = list.pop()
count = 0
for i in range(num):
    if list:
        if a >= list[-1]:
            list.pop()
            count += 1
        else:
            a = list.pop()
print(num-count)