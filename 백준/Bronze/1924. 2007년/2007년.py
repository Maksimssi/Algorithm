x, y = map(int, input().split())

dict1 = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
dict2 = {1:'MON',2:'TUE',3:'WED',4:'THU',5:'FRI',6:'SAT',0:'SUN'}
total = 0

for i in range(1, x):
    if x == 1:
        total += 0
    else:
        total += dict1[i]
total += y

print(dict2[total%7])