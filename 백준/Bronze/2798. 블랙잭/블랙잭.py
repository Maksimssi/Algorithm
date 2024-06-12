import sys

cards, goal = map(int, input().split())

card_list = list(map(int,sys.stdin.readline().split()))
result = 0

for i in range(cards):
    for j in range(i+1,cards):
        for k in range(j+1,cards):
            if not result:
                result = card_list[i]+card_list[j]+card_list[k]
            elif goal >= card_list[i]+card_list[j]+card_list[k]:
                if abs(goal - result) > abs(goal - (card_list[i]+card_list[j]+card_list[k])):
                    result = card_list[i]+card_list[j]+card_list[k]
print(result)