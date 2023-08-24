import sys
sys.stdin = open('sum_neighbor_in.txt','r')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())  #배열 길이
    arr = list(map(int, input().split()))
    i = 0
    max_v =  -1000
    for _ in range(N - 1):
        section_sum = sum(arr[0 + i : 2 + i]) #슬라이싱 범위 주의
        if max_v <= section_sum:
            max_v = section_sum
        i += 1


    print(f'#{tc} {max_v}')
