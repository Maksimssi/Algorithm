word = input().upper()

word_dict = {}

for i in word:
    if i in word_dict:
        word_dict[i] += 1
    else:
        word_dict[i] = 1

max_value = max(word_dict.values())

# 중복값을 저장하지 않기 위해 빈 set() 생성
max_char = set()
for i in word:
    if max_value == word_dict[i]:
        max_char.add(i)

# set은 인덱스를 지정하여 값을 가져올 수 없으므로 list로 변환
result = list(max_char)
if len(max_char) == 1:
    print(result[0])
else:
    print('?')