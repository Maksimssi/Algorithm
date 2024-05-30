input_num = input().split()

reversed_num1 = int(input_num[0][::-1])
reversed_num2 = int(input_num[1][::-1])

print(reversed_num1) if reversed_num1 > reversed_num2 else print(reversed_num2)