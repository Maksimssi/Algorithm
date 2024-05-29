num = input()
dice = [num[:1],num[2:3],num[4:5]]
dice.sort()

if dice[0] == dice[1] and dice[0] == dice[2]:
    print(10000 + (int(dice[0]) * 1000))
elif dice[0] == dice[1] or dice[0] == dice[2] or dice[1] == dice[2]:
    print(1000 + (int(dice[1]) * 100))
else:
    print(int(dice[2]) * 100)