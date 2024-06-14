how_many = int(input())
height_list = list(map(int,input().split()))
max_height, kill_count, length, break_count = 0, 0, 0, 0

for height in height_list:
    length += 1
    if max_height == 0:
        max_height = height
    elif max_height > height:
        kill_count += 1
    elif max_height < height:
        if kill_count >= (len(height_list) - length):
            break_count = kill_count
            break
        else:
            kill_count = 0
            max_height = height

print(kill_count if break_count == 0 else break_count)