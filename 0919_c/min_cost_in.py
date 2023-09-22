import sys
sys.stdin = open("min_cost_in.txt",'r')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int,input().split())))
    cost = 0
    min_cost = 999999 #임의의 min값
    visited = [0] * N #방문한 열 표시
    def backtrack(cnt): #cnt = 다음 행으로 넘어가면서
        global cost, min_cost
        #가지치기
        #여태까지 계산한 값이 min_cost 보다 크면 계산 멈춤
        if cost > min_cost:
            return
        if cnt == N:
            if cost < min_cost:
                min_cost = cost
            return
        for j in range(N):
            if not visited[j]: #방문하지 않은 열이면
                cost += arr[cnt][j]
                visited[j] = 1
                backtrack(cnt + 1)
                cost -= arr[cnt][j] #초기화
                visited[j] = 0 #visited 초기화

    backtrack(0)
    print(f'#{tc} {min_cost}')
