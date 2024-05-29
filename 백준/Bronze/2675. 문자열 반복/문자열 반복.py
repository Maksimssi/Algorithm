n = int(input())

for i in range(n):
    value = input().split()

    R = int(value[0])
    S = value[1]
    result = ''

    for j in range(len(S)):
        result += R * S[j]
    print(result)