#인접 행렬
# 장점: 구현이 쉽다
# 단점 : 메모리 낭비 (갈 수 없는 곳도 표시)
# 갈 수 없으면 사용을 안 하면 그만인 것을...
graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 1, 0]
]


def dfs_stack(start):
    #방문했던 지점 : 다시 방문하면 X
    visited = []
    stack = [start]

    while stack:
        now = stack.pop()
        #이미 방문한 지점이라면 continue
        if now in visited:
            continue

        #방문하지 않은 지점이라면
        visited.append(now)

        #갈 수 있는 곳들을 stack에 추가
        for next in range(5):
            #연결이 안 되어 있다면 continue
            #취향의 차이. 가능할 때를 위주로 짜도 됨
            if graph[now][next] == 0:
                continue

            if next in visited:
                continue

            stack.append(next)
    return visited
print(*dfs_stack(0))