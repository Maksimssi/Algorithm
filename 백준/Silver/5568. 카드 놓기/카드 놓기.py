from itertools import permutations

total_card_count = int(input())
select_card_count = int(input())
card_list = [input() for _ in range(total_card_count)]

# set은 중복 제거해줌..
card_combinations = set()
for i in permutations(card_list, select_card_count):
    card_combinations.add("".join(i))

print(len(card_combinations))