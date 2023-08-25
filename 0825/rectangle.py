#네모네모 영역 나누기
M = 7
arr2 = [[0] * M for _ in range(M)]

for i in range(1, M):
    for j in range(1, M):
        #첫번째 사각형
        for r in range(0, i):
            for c in range(0, j):
                arr2[r][c] = 0
        # 두번째 사각형
        for r in range(0, i):
            for c in range(j, M):
                arr2[r][c] = 1

        # 세번째 사각형
        for r in range(i, M):
            for c in range(0, j):
                arr2[r][c] = 1

            # 네번째 사각형
        for r in range(i, M):
            for c in range(j, M):
                arr2[r][c] = 0

        #그려서 바로 뿌려야 한다
        for line in arr2:
            print(*line)
        print("-------------------------")