from collections import deque
start = 5
end = 17
MAX_val = 10**5
visited = [0] * (MAX_val+1)

def bfs(start, end):
    global MAX_val
    q = deque()
    q.append(start)
    while q:
        x = q.popleft()
        if x == end:
            return visited[nx]

        for nx in [x-1, x+1, 2*x]:
            if not visited[nx]:
                visited[nx] = visited[x] + 1
                q.append(nx)


result = bfs(start,end)

print(result)
