import sys
sys.stdin = open('safty_area_in.txt','r')
from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

#최대 빗물 높이 - array의 max값 까지만 계산하면 됨 (그 이후로는 모두 잠기므로)
#임의의 max값
max_v = 0
for r in range(N):
    for c in range(N):
        if max_v < arr[r][c]:
            max_v = arr[r][c]

#delta 접근 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

#BFS 함수
def bfs(r, c, num): #빗물 높이 값 num
    q = deque()
    #조건에 맞는 r,c 만 BFS에 들어옴 - 바로 queue 에 넣으면 됨
    q.append([r,c])
    visited[r][c] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dr[i], y + dc[i]
            if nx in range(N) and ny in range(N):
                if num < arr[nx][ny] and not visited[nx][ny]:
                    q.append([nx,ny])
                    visited[nx][ny] = 1

shelter_lst = []
for num in range(max_v):
    cnt = 0 #안전 영역 수 count를 위한 변수
    visited = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if arr[r][c] > num and not visited[r][c]: #높이가 num 보다 높고 아직 탐색하지 않은 영역에 대해
               bfs(r,c,num) #bfs
               cnt += 1
    shelter_lst.append(cnt)

print(max(shelter_lst))
