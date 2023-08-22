arr = [1, 2, 3, 4, 5]
M = 3
visited = [0 for _ in range(len(arr))]
result = []
max_v = -1

def dfs(cnt):
    global max_v

    if cnt == M:
        if max_v <= sum(result):
            max_v = sum(result)
        return

    for i in range(len(arr)):
        if visited[i] == 0:
            visited[i] = 1  # 중복 제거
            result.append(arr[i])

            dfs(cnt+1)  # 다음 깊이 탐색

            visited[i] = 0  # 탐사 완료 후 다시 초기화
            result.pop()  # 탐사한 내용 제거

dfs(0)
print(max_v) #global 선언 했으니까 이렇게 쓸 수 있음