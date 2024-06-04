num = int(input())

score = list(map(int,input().split()))

result = 0

max_score = max(score)


for i in range(num):
    result += score[i] / max_score * 100

print(result/num)