name = input().split('-')
result = ''

for i in range(len(name)):
    result += (name[i][:1])

print(result)