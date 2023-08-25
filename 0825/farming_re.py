import sys
sys.stdin = open('farming_in.txt','r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_diff = 9999999

    for i in range(1, N): # 가로 방향 구분선, 최솟값 1 최댓값 N - 1
        for j in range(1, N): #세로 방향 구분선  최솟값 1 최댓값 N - 1

            #1번 사각형
            sum1 = 0
            for r in range(0, N):
                for c in range(j ,N):
                    sum1 += arr[r][c]

            #2번 사각형
            sum2 = 0
            for r in range(0, i):
                for c in range(0, j):
                    sum2 += arr[r][c]

            #3번 사각형
            sum3 = 0
            for r in range(i, N):
                for c in range(0, j):
                    sum3 += arr[r][c]

            sum_lst = [sum1, sum2, sum3]

            #최댓값과 최솟값 구하기
            max_sum, min_sum = max(sum_lst), min(sum_lst)

            #최댓값 최솟값 사이 차이
            diff = max_sum - min_sum

            if diff < min_diff:
                min_diff = diff
    #출력
    print(f'#{tc} {min_diff}')
