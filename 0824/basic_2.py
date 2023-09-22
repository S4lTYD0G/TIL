import sys
sys.stdin = open('basic_2_in.txt','r')
T = int(input())
for tc in range(1, T + 1):
    arr = list([0] *10 for _ in range(10))
    r, c, width, height = map(int, input().split())

    i = 1
    for Y in range (height):
        if Y % 2 == 0 : #짝수 줄일 때
            for x in range(c, c + width):
                arr[r][x] += i
                i += 1
            r += 1
        elif Y % 2 != 0: #홀수 줄일 때
            for x in range(c + width -1 , c - 1, -1): #오->왼 방향
                arr[r][x] += i
                i += 1
            r += 1
    #출력
    print(f'#{tc}')
    for line in arr:
        print(*line)
