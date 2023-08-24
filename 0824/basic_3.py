import sys
sys.stdin = open('basic_3_in.txt','r')
T = int(input())
for tc in range(1, T + 1):
    arr = list([0] *10 for _ in range(10))
    r, c, N = map(int, input().split())

    #arr[r][c]에서 시작하는 오른쪽 아래 방향의 대각
    for i in range(N):
        arr[r][c] = 1
        r += 1
        c += 1

    #for문 돌고 나면 r,c가 오른쪽 아래 대각(의 대각선 한 칸 밑)에 가있음
    # r, c 위치 재설정
    r -= N
    c -= 1
    for i in range(N):
        arr[r][c] =1
        r += 1
        c -= 1

    # 출력
    print(f'#{tc}')
    for line in arr:
        print(*line)
