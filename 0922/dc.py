
def backtrack(cnt, success):
    global max_v

    if success * 100 < max_v:
        return

    if cnt == N:
        # 각 요소들 곱하기
        result = success * 100
        if max_v < result:
            max_v = result
        return


    for i in range(N):

        if not visited[i]:  # 방문하지 않았으면
            if arr[cnt][i] == 0:  # 요소 중 0이 있으면 pass
                continue
            success *= (arr[cnt][i] * 0.01)
            visited[i] = 1  # 방문열 표시
            backtrack(cnt + 1, success)
            visited[i] = 0  # 방문 열 초기화
            success /= (arr[cnt][i] * 0.01)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 임의의 큰 수
    max_v = -1
    # 방문한 열 저장
    visited = [0 for _ in range(N)]
    backtrack(0, 1)
    print(f'#{tc}{max_v:.6f}')