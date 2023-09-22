import sys
sys.stdin = open('grouping_in.txt','r')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    p = [i for i in range(N + 1)] #초기값 설정- 자기 자신 가리키게
    print(p)
    #0번은 안쓴다

    def find_set(x):
        if x != p[x]:
            p[x] = find_set(p[x])
        return p[x]

    ans = N
    for i in range(0, M*2, 2):
        u,v = arr[i], arr[i+1]

        a = find_set(u)
        b = find_set(v)

        if a == b: continue
        p[b] =  a
        ans -= 1

    print(f'#{tc} {ans}')