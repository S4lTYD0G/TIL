import sys
sys.stdin = open("area_in.txt",'r')
from collections import deque

q = deque()
#세로, 가로, 사각형 수
#세로(행) - r 값 접근. 가로(열) - c값 접근
M, N, rec  = map(int, input().split())
#행렬 만들기
arr = [[1] * N for _ in range(M)]
# 사각형 좌표 입력 받기
for i in range(rec):
    x1, y1, x2, y2 = map(int, input().split())
    width = x2 - x1
    height = y2 - y1
    #왼쪽 상단이 0.0 일 때  사각형의 왼쪽 상단 좌표 (r, c)
    #r, c 값 주의
    r = M - y1 - height
    c = x1
    for x in range(r, r + height): #0, 1
        for y in range(c, c + width):
            arr[x][y] = 0
    # 갈 수 없는 영역(직사각형)표시하기

#delta 접근 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

#BFS
num_area = 0
area = 0
area_lst = [] #영역 넓이 담을 list
for r in range(M):
    for c in range(N):
        if arr[r][c] == 1:
            q.append([r,c])
            area = 1
            arr[r][c] = 0
            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx, ny = x + dr[i], y + dc[i]
                    if nx in range(M) and ny in range(N) and arr[nx][ny] == 1:
                        q.append([nx,ny])
                        arr[nx][ny] = 0
                        area += 1
            num_area += 1
            area_lst.append(area)

area_lst.sort()
print(num_area)
print(*area_lst)
