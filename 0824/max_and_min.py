import sys
sys.stdin = open('max_and_min_in.txt','r')
T = int(input())
for tc in range(1, T+1):
    N = int(input()) #배열 길이
    arr = list(map(int, input().split()))

    #최솟값은 이렇게 찾으면 됨
    min_idx = arr.index(min(arr))
    #index()함수 쓰면 같은 값이 존재할 때 가장 가까운 값의 idx 만 따옴...
    max_v = max(arr)

    # for i in arr로 접근하면 max값의 idx 찾을 수 없음
    for i in range(N):
        if max_v == arr[i]: #배열 끝까지 순회하며 max값과 동일한 숫자 중 idx가 큰 값 찾기
            max_idx = i

    print(f'#{tc} {abs(max_idx - min_idx)}')
