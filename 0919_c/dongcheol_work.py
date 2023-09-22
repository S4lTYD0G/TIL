import sys
sys.stdin = open('dongcheol_work_in.txt','r')
T = int(input())
for tc in range(1, T+1):
    N = int(input()) #열의 갯수
    arr = [list(map(int, input().split())) for _ in range(N)]
    work = []
    visited = [0] * N #방문한 열 표시
    def backtrack(cnt):
        if cnt == N:
            print(work)
            return
        for j in range(N):
            #방문하지 않은 열이면
            if not visited[j]:
                work.append(arr[cnt][j])
                visited[j] = 1
                backtrack(cnt + 1)
                visited[j] = 0
                work.pop()
    backtrack(0)
    