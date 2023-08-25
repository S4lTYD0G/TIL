N = 7
arr = [[0] * N for _ in range(N)]
#====================================================
# #좌상단 좌표
r1, c1 = 1, 1
h, w = 4, 5
#우하단 좌표
r2 = r1 + h - 1
c2 = c1 + w - 1

for c in range(c1, c1 + w):
    arr[r1][c] =1
    arr[r2][c] =1

for r in range(r1 + 1, r2):
    arr[r][c1] =2
    arr[r][c2] =2
 # =====================================================



for line in arr:
    print(*line)