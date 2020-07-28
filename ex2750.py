case = int(input())
nl = list()
for i in range(case):
    num = int(input())
    nl.append(num)

while nl:
    a = int(min(nl))
    print(a)
    nl.remove(a)
