import sys

sys.stdin = open('dongcheol_work_in.txt', 'r')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 열의 갯수
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = -1 #임의의 큰 값
    visited = [0] * N  # 방문한 열 표시


    def backtrack(cnt, work):
        global max_v
        if cnt == N:
            if max_v < work:
                max_v = work
            return
        if work < max_v:
            return
        for j in range(N):
            # 방문하지 않은 열이면
            if not visited[j]:
                work *= (arr[cnt][j] * 0.01)
                visited[j] = 1
                backtrack(cnt + 1, work)
                visited[j] = 0 #visited 초기화


    backtrack(0,1)
    print(f'#{tc}',end=' ')
    print("{:.6f}".format((max_v)*100))