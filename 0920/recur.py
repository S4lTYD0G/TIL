graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 1, 0]
]

#DFS 재귀
visited = [0] * 5
path = []

def dfs(now):
    visited[now] = 1
    #기저조건
    print(now)
    #들어가기 전
    #인접한 노드들을 방문
    for next in range(5):
        if graph[now][next] == 0:
            continue

        if visited[next]:
            continue

        dfs(next)
    #함수 호출
    #돌아와서