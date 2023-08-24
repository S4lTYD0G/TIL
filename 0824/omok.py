import sys
sys.stdin = open('omok_in.txt','r')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    #delta 접근 - 우. 우하 대각선, 하, 좌하 대각선
    dr = [0, 1, 1, 1]
    dc = [1, 1, 0, -1]
    flag = 0
    cnt = 0
    x, y = 0, 0 #시작 좌표
    for x in range(N):
        for y in range(N):
            if arr[x][y] == 'o':
                for i in range(4):
                    cnt = 0
                    for j in range(1, 5):
                        nx, ny = x + dr[i] * j, y + dc[i] * j
                        if nx in range(N) and ny in range(N):
                            if arr[nx][ny] == 'o':
                                cnt += 1
                    if cnt == 4: #arr[x][y] =='o' 일 때만 실행되므로 4까지만 세면 됨 
                         flag = 1
    if flag ==1:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')