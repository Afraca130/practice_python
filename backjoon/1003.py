case = int(input())
fibList = [(1, 0), (0, 1)]

for i in range(2, 41):
    addList = (fibList[i-2][0] + fibList[i-1][0],
               fibList[i-2][1] + fibList[i-1][1])
    fibList.append(addList)

for i in range(0, case):
    n = int(input())
    print(fibList[n][0], fibList[n][1])
