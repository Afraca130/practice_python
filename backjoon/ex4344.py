case = int(input())
for i in range(case):
    grade = list(map(int, input().split(' ')))
    cnt = 0
    num = grade.pop(0)
    avg = sum(grade)/num
    for j in range(num):
        if grade[j] > avg:
            cnt += 1
    result = "{:0.3f}%".format(cnt/num*100)
    print(result)
