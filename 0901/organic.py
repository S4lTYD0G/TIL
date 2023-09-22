import sys
sys.stdin = open('organic_in.txt','r')
from collections import deque

T = int(input())
for tc in range(1, T + 1):
    #가로, 세로, 배추 위치
    N, M, point = map(int, input().split())
    # 0으로 채워진 N * M 행렬 만들기
    arr = [[0] * M for _ in range(N)]
    #배추 위치 표시하기
    for _ in range(point):
        r, c = map(int, input().split())
        arr[r][c] = 1
    #BFS 탐색을 위한 queue
    q = deque()
    #delta 접근 - 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    cnt = 0 #배추가 심어진 영역 표시
    #BFS
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 1:
                q.append([r, c])
                arr[r][c]  = 0 #0으로 초기화 안하면 무한루프 돈다...
                while q:
                    x, y = q.popleft()
                    for i in range(4):
                        nx, ny = x + dr[i], y + dc[i]
                        if nx in range(N) and ny in range(M) and arr[nx][ny] == 1:
                            q.append([nx, ny])
                            arr[nx][ny] = 0
                cnt += 1


    print(cnt)
