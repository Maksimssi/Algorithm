# i * i 번 배열 만들고 범위의 합 구하기

range1, range2 = map(int, input().split())

num_list = [0]
sum_num, count = 0, 0

for i in range(1,range2+1):
    for j in range(i):
        num_list.append(i)
        count += 1
    if count > range2:
        break

for i in range(range1, range2+1):
    sum_num += num_list[i]

print(sum_num)