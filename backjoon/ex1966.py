case = int(input())
result = []

for i in range(0, case):
    count = 0
    n, m = map(int, input().split(' '))
    queue = list(map(int, input().split(' ')))
    while queue[m] != 0:
        if queue[count] == max(queue):  # 우선 순위에서 가장 먼저해야하는것
            queue[count] = 0  # 인쇄된 것들은 0으로 처리한다.
            if queue[m] == 0:
                print(queue.count(0))
                # 0의 갯수 = 프린트 된 갯수 이므로 m번째의 작업이 프린트 될때의 0의 갯수는 m번쨰 작업물의 프린트 순서가 된다.
                break

        count += 1
        if count >= len(queue):  # count 숫자가 넘어가면 처음으로
            count = 0
