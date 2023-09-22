import sys
sys.stdin = open('farming_in.txt','r')
from itertools import combinations

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    #필요한 것: 죄상단 좌표, 우하단 좌표
    #특징 : r은 모두 순회(세로로 긴 행렬),  c = 1부터 (N-4), 0행렬 들어가면 안 됨
    min_diff = 999999
    for vert_line in range(1, N):
        #여기서 sum_lst 리스트가 초기화 되면 안됨 (값 쌓임)
        sum_3 = 0
        for r in range(N):
            for c in range(N-vert_line, N): # 3, 4
                sum_3 += arr[r][c]
        #print(sum_3)
        #가로 구하는거 다시 생각해서 정리해 ~
        for horr_line in range(1, N):
            sum_1 = 0
            sum_2 = 0
            for c in range(N - vert_line): #세로 범위 공유!!
                for r in range(horr_line):
                    sum_1 += arr[r][c]
                for r in range(horr_line, N):
                    sum_2 += arr[r][c]
            sum_lst = [sum_3, sum_2, sum_1]
            #차이의 최솟값 찾기

            max_v , min_v = max(sum_lst) , min(sum_lst)
            diff = max_v - min_v
            if diff < min_diff:
                min_diff = diff
    print(f'#{tc} {min_diff}')
