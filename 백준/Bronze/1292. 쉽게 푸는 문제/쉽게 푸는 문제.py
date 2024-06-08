first, second = map(int, input().split())
num_list = [1]

for i in range(2,second):
    for j in range(i):
        num_list.append(i)
print(sum(num_list[first-1:second]))