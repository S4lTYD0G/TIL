import sys
sys.stdin = open('min_dist_in.txt','r')
T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    G =[[]for _ in range(N + 1)]
    for _ in range(E):
        u,v,weight = map(int, input().split())
        #유향
        G[u].append((v,weight))
        #가중치 - 방문정보 X 거리를 저장하는...
    #초기값 설정 중요!!!!
    D = [0xfffff] * (N + 1)
    # D[v] => 출발점에서 v 정점까지 최단 거리
    #아직 어떤 경로도 발견하지 못했다
    #출발점의 D 값: 0
    D[0] = 0
    # 처음에 출발점을 넣기
    # BFS 처럼 한다
    Q = [0]
    while Q:
        u = Q.pop(0)
        #인접 정점 찾기
        for v, weight in G[u]:
            #u,v 간선 완화
            if D[v] > D[u] + weight:
                #새로운 경로 발견~
                D[v] = D[u] + weight
                Q.append(v)
    print(f'#{tc} {D[N]}')