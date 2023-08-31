from collections import deque
import sys
sys.stdin = open('adress_in.txt','r')
input = sys.stdin.readline
N = int(input())
arr = [list(input()) for _ in range(N)]
q = deque()
#delta 접근 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

#처음 집의 위치 que에 넣어야 while문이 돈다는 문제..
cnt_group = 1 #단지 수 세는 변수, 단지 넘버 표시를 위해 1부터 시작하나 정답은 -1 해줘야 함
num_of_house = []
for r in range(N):
    for c in range(N):
        if arr[r][c] == '1':
            q.append([r,c]) #좌표 저장
            house = 1 #집 수 초기화
            arr[r][c] = cnt_group #단지 넘버로 채우기

            while q:
                start = q.popleft()
                x, y = start[0], start[1]
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if nx in range(N) and ny in range(N) and arr[nx][ny] == '1':
                        q.append([nx, ny])
                        arr[nx][ny] = cnt_group
                        house += 1
            cnt_group += 1 #q가 빌 때마다 count += 1
            num_of_house.append(house)




print(cnt_group-1)
num_of_house.sort()
for _ in range(len(num_of_house)):
    print(num_of_house[_])