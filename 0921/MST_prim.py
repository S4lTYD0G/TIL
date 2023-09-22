
import sys
sys.stdin = open("MST_in.txt",'r')
import heapq

def prim(start):
    heap = []
    MST = [0] * (V+1)
    #weight, start 좌표 순으로
    heapq.heappush(heap,(0, start))
    sum_weight = 0

    while heap:
        #가장 작은 가중치를 가진 정점 순서대로 꺼냄
        weight, v = heapq.heappop(heap)


        if MST[v]:
            continue
        MST[v] = 1

        sum_weight += weight

        for n in G[v]:
            #갈 수 없거나 이미 방문했다면 pass
            if MST[n[1]]:
                continue
            heapq.heappush(heap, (n[0],n[1]))
    return sum_weight


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    #연결 리스트
    G = [[]  for _ in range(V+1)]
    for _ in range(E):
        start, end, weight = map(int, input().split())
        #연결 상태, 가중치 저장
        #0이면 연결 안된 것
        #양방향 그래프
        G[start].append((weight,end))
        G[end].append((weight,start))
    result = prim(0)
    print(f'#{tc} {result}')