big_num, small_num = map(int,input().split())

result = ''
another = 0

for i in range(2, small_num):
    if big_num % i == 0:
        result = 'BAD'
        another = i
        break


print(result+' '+str(another) if result=='BAD' else 'GOOD')