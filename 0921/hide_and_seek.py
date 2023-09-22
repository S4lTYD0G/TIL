import sys
from collections import deque
input = sys.stdin.readline

def hide_and_seek(start, end):
    q = deque()
    q.append(start)
    dist[start] = 1
    while q:
        #현재 위치
        x = q.popleft()
        if x == end:
            return dist[nx]
        for nx in (x-1, x+1, 2*x):
            if 0<= nx <= max_v+1 and not dist[nx]:
                q.append(nx)
                dist[nx] = dist[x] + 1


start, end = map(int, input().split())
max_v = 10**5
dist = [0 for _ in range(max_v+1)]
result = hide_and_seek(start,end)
print(result-1)