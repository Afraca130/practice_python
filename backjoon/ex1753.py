import sys


def min_heapify(i):
    global heap
    left = 2 * i
    right = left + 1

    if left <= len_heap and heap[left][1] < heap[i][1]:
        smallest = left
    else:
        smallest = i

    if right <= len_heap and heap[right][1] < heap[smallest][1]:
        smallest = right

    if smallest != i:
        temp = heap[i]
        heap[i] = heap[smallest]
        heap[smallest] = temp
        min_heapify(smallest)


def pop():
    global heap, len_heap
    result = heap[1]
    heap[1] = heap[len_heap]
    del heap[len_heap]
    len_heap -= 1
    l = len_heap
    while l > 0:
        min_heapify(l)
        l = l // 2
    return result


# 값 초기화
v, e = map(int, sys.stdin.readline().rstrip().split())
start = int(sys.stdin.readline().rstrip())

# edges[i]: [j(연결된 node), w(가중치)]
edges = [[] for _ in range(v)]
for _ in range(e):
    s, e, w = map(int, sys.stdin.readline().rstrip().split())
    edges[s-1].append([e-1, w])

INF = 10 * v + 1

visited = []  # 방문한 node들 저장
dist = [INF for _ in range(v)]  # dist[i]: i node까지의 최단 거리
dist[start-1] = 0  # 시작 node까지 최단거리 초기화

# 전체 node들까지의 거리를 INF로 초기화하여 heap에 추가한다.
heap = [None]
heap += [[i, INF] for i in range(v)]
heap[start][1] = 0
len_heap = v

# 우선 정렬한다.
for i in range(int(len_heap/2), 0, -1):
    min_heapify(i)

# popped = [index, 거리]
popped = pop()
while popped[1] != INF:
    # adj: index와 연결된 nodes
    i = popped[0]
    adj = edges[i]
    visited.append(i)

    for [j, w] in adj:
        # i -> j에 대해 dist[j] > dist[i] + w 때 Update 해준다.
        if dist[j] > dist[i] + w:
            dist[j] = dist[i] + w
            heap.append([j, dist[j]])
            len_heap += 1
            loop = len_heap
            while loop > 0:
                min_heapify(loop)
                loop = loop // 2

    # 다음으로 넘어갈 node를 결정한다.
    # POP 결과가 distance보다 길거나 이미 방문한 node라면 다시 Pop한다.
    while popped[1] > dist[popped[0]] or popped[0] in visited:
        popped = pop()

# 출력한다.
for dis in dist:
    if dis == INF:
        print("INF")
    else:
        print(dis)
