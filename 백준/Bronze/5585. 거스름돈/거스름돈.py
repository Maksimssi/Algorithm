price = int(input())

account = 1000
my_changes = account - price
changes_list = [500, 100, 50, 10, 5, 1]
money_count = 0

for changes in changes_list:
    money_count += my_changes // changes
    my_changes %= changes

print(money_count)