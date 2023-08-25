import sys
sys.stdin = open('section_sum_in.txt','r')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    min_diff = 99999999
    #3 구간으로 나누기
    # 첫번째 구간 : 0 안됨 ~ 1 부터 N-2 까지 (N-2 값이 들어갸야 함)
    for i in range(1, N - 1):
        for j in range (i + 1, N):
            sum1 = sum(arr[:i])
            sum2 = sum(arr[i:j])
            sum3 = sum(arr[j:])
            sum_lst = [sum1, sum2, sum3]

            #최대, 최솟값 구하기
            max_v = max(sum_lst)
            min_v = min(sum_lst)

            diff = max_v - min_v
            if diff < min_diff:
                min_diff = diff

    print(f'#{tc} {min_diff}')