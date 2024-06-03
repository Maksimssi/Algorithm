n, m = map(int,input().split())

array1 = []
array2 = []

for i in range(n):
    array1.append(list(map(int,input().split())))

for i in range(n):
    array2.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        print(array1[i][j] + array2[i][j],end=' ')
    print()