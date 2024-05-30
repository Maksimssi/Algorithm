count = int(input())
fruit = {'STRAWBERRY':0,'BANANA':0,'LIME':0,'PLUM':0}
count2 = 0

for i in range(count):
    fruit_name, quantity = input().split()
    fruit[fruit_name] += int(quantity)

print('YES') if 5 in fruit.values() else print('NO')