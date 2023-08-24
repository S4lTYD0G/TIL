import sys
sys.stdin = open('bombing_in.txt','r')
T = int(input())
for tc in range(1, T + 1):
    N, num_bomb = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    #delta 접근 - 좌 우 상 하
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    total_sum = 0
    #폭탄 i 개에 대하여
    for i in range(num_bomb):
        x, y, power = map(int, input().split())
        sum = arr[x][y]
        for delta in range(4):
            for p in range(1, power + 1): #범위 주의, 0 넣으면 0 곱하게 됨
                nx, ny = x + dr[delta] * p,  y + dc[delta] * p
                if nx in range(N) and ny in range(N): #범위 안에 있으면
                    sum += arr[nx][ny]
                    arr[nx][ny] = 0
        total_sum += sum #위치 주의 - for문 다 돌고 나서

    print(f'#{tc} {total_sum}')