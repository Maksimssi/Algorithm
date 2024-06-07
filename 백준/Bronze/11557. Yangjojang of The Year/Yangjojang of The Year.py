tests = int(input())

name_list = []
soju_list = []
result = []
max_soju = 0
for i in range(tests):
    schools = int(input())

    for j in range(schools):
        input_val = input().split()
        name_list.append(input_val[0])
        soju_list.append(int(input_val[1]))

        max_soju = max(soju_list)


    result.append(name_list[soju_list.index(max_soju)])
    name_list.clear()
    soju_list.clear()

for r in result:
    print(r)