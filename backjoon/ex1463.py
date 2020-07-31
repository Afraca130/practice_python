num = input('숫자를 입력하세요')
counter = 0

if num % 3 == 0:
    num /= 3
else :
    if num % 2 == 0:
        num /= 2
    else :
        num -= 1

