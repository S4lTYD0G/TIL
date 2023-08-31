N = 3
D = [[0] * N for _ in range(N)]

def dfs(r, c):
    #(r,c)에서 선택지는 두가지
    #오른쪽으로 간다
    if r == N - 1 and c == N - 1 : #도착
        D[r][c] = 1
        for line in D:
            print(*line)
        D[r][c] = 0
        print("=====================")

    else:
        D[r][c] = 1

        if c + 1 in range(N):
            dfs(r, c + 1)

        #아래
        if r + 1 in range(N):
            dfs(r + 1, c)

        D[r][c] = 0

dfs(0,0)