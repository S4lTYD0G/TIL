#4, 7
import sys
sys.stdin = open('im_ex_in.txt','r')
T = int(input())
#델타 접근 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]


    # A가 있을 때
    for r in range(N):
        for c in range(N):
            if arr[r][c] == "A":
                for i in range(4):
                    nr, nc = r + dr[i] , c + dc[i]
                    if nr in range(N) and nc in range(N):
                        if arr[nr][nc] == "H":
                            arr[nr][nc] = "X"
    #B가 있을 때
    for r in range(N):
        for c in range(N):
            if arr[r][c] == "B":
                for i in range(4):
                    for j in range(1, 3):
                        nr, nc = r + dr[i] * j , c + dc[i] * j
                        if nr in range(N) and nc in range(N):
                            if arr[nr][nc] == "H":
                                arr[nr][nc] = "X"
    #C가 있을 때
    for r in range(N):
        for c in range(N):
            if arr[r][c] == "C":
                for i in range(4):
                    for j in range(1, 4):
                        nr, nc = r + dr[i] * j , c + dc[i] * j
                        if nr in range(N) and nc in range(N):
                            if arr[nr][nc] == "H":
                                arr[nr][nc] = "X"
    cnt = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == "H":
                cnt += 1
    print(f'#{tc} {cnt}')


