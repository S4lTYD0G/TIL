import heapq

def prim(start):
    heap = []
    MST = 0 * V
    #weight, start
    heapq.heappush(heap, (0, start))

    while heap:
        #가장 작은 가중치를 가진 정점을 꺼냄
        weight, v = heapq.heappop(heap)

        #방문했는지 체크
        if MST[v]:
            continue
        MST[v] = 1

        #갈 수 있는 노드들을 체크
        for next in range(V):
            #갈 수 없거나 이미 방문했다면 pass
            if graph[v][next] == 0 or MST[next]:
                continue
            heapq.heappush(heap,(graph[v][next], next))
'''
1. 정점 갯수 7
2. 간선 갯수 11
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''
V, E = map(int,input().split())
# 인접행렬 - 시간 공간 여유로울 때...
graph = [[0] * [V] for _ in range(V)]
# 뒤쪽 입력에 따라 하나하나 연결
for _ in range(E):
    #from, to, weight
    f, t, w = map(int.input().split())
    #시작, 도착, 가중치
    graph[f][t] = w
    #양방향 그래프
    graph[t][f] = w
