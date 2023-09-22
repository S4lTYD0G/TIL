import sys
sys.stdin = open('basic_5_in.txt','r')
T = int(input())
for tc in range(1, T + 1):
    arr = list([0] *10 for _ in range(10))
    r, c, N = map(int, input().split())

    i = 1
    for x in range(r, r + N):
        for y in range(c, c + N):
            arr[x][y] += i
            i += 1

    # 출력
    print(f'#{tc}')
    for line in arr:
        print(*line)
