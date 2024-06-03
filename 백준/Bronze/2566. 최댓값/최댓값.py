import sys

list = []
max_list = {}

for i in range(9):
       num = sys.stdin.readline()
       list.append(num.split())
       max_list[(int(max(list[i])))] = [i+1,list[i].index(max(list[i]))+1]

max_val = max(max_list.keys())

print(max(max_list))
print(max_list[max_val][0], max_list[max_val][1])