input_list = [input() for i in range(5)]

list_length = max(len(i) for i in input_list)

for i in range(list_length):
    for j in range(5):
        if i < len(input_list[j]):
            print(input_list[j][i],end='')