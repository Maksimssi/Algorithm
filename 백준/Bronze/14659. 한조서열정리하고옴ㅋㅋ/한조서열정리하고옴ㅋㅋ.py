n = int(input())
hights = list(map(int, input().split()))

cnt = 0
maxNum = hights[0]
for i in range(n):
    if maxNum > hights[i]:
        cnt += 1
    elif maxNum < hights[i]:
        if cnt >= n-i:
            break
        else:
            maxNum = hights[i]
            cnt = 0

print(cnt)