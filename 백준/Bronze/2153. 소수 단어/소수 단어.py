num = 0
string = input()

# 입력된 문자를 숫자로 변환
for i in range(len(string)):
    strong = string[i]
    if string[i].isupper():
        num += ord(strong)-38
    elif string[i].islower():
        num += ord(strong)-96

# 소수인지 확인.
for i in range(2,num//2+4):
    if num ==1 or num==2 or num ==3:
        print('It is a prime word.')
        break
    if num%i == 0:
        print('It is not a prime word.')
        break
    elif i == num//2:
        print('It is a prime word.')
        break