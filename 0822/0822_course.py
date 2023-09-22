N, M = map(int, input().split())
visited = [0 for _ in range(N)]
arr = []

def dfs(cnt):
    if cnt == M:
        print(*arr)
        return

    for i in range(0, N):
        if visited[i] == 0:
            visited[i] = 1  # 중복 제거
            arr.append(i+1)

            dfs(cnt+1)  # 다음 깊이 탐색

            visited[i] = 0  # 탐사 완료 후 다시 초기화
            arr.pop()  # 탐사한 내용 제거

dfs(0)