sum = 0
input_num = []
for i in range(10):
    input_num.append(int(input()))


for i in range(10):
    if sum == 0:
        sum += input_num[i]
    elif abs(100 - sum) > abs(100 - (sum+input_num[i])):
        sum += input_num[i]
    elif abs(100 - sum) == abs(100 - (sum+input_num[i])):
        sum += input_num[i]
    else:
        break
print(sum)
