import sys
sys.stdin = open('basic_4_in.txt','r')
T = int(input())
for tc in range(1, T + 1):
    arr = list([0] *10 for _ in range(10))
    r, c, width, height = map(int, input().split())

    i = 1
    for y in range(c, c + width): #범위 주의
        for x in range(r, r + height):
            arr[x][y] += i
            i += 1
    # 출력
    print(f'#{tc}')
    for line in arr:
        print(*line)
