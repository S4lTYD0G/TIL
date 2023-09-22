N = 8
arr = list([0] * N for _ in range(N))


#상 우 하 좌 순으로
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]
r, c = 5, 5
for i in range(8):
    nr, nc = r + dr[i], c + dc[i]
    if nr in range(N) and nc in range(N):
        arr[nr][nc] += 1

for line in arr:
    print(line)