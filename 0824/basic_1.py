import sys
sys.stdin = open('basic_1_in.txt','r')
T = int(input())
for tc in range(1, T + 1):
    arr = list([0] *10 for _ in range(10))
    r, c, N = map(int, input().split())

    #열 방향으로 (왼->오), 고정 : r
    for x in range(c, c + N ):
          arr[r][x] = 1
    #행 방향으로 +1 , 고정 : c
    for y in range(r, r + N):
        arr[y][c] = 1

    #하단 오른쪽 끝 점
    r, c =  r + (N-1), c + (N-1)
    #열 방향으로 (오->왼), 고정 : r
    for x in range(c, c-N, -1):
        arr[r][x] = 1
    #행 방향으로 (아래-> 위), 고정: c
    for y in range(r, r-N, -1):
        arr[y][c] = 1

    #출력
    print(f'#{tc}')
    for line in arr:
        print(*line)
