import sys
sys.stdin = open('swea_10760_in.txt','r')
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split()) #행, 열
    arr = [list(map(int, input().split())) for _ in range (N)]
    ans = 0 #착륙 지점 수

    r,c = 0, 0      #초기값

    #주변 8방향 delta 접근
    # 상 우 하 좌
    dr = [ -1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, 1, 1, 1, 0, -1, -1, -1]

    for r in range (N):
        for c in range (M):
            center_v = arr[r][c]    # 비교 대상 중앙 값
            cnt = 0                 # 중앙 값보다 작은 주변 값의 수를 저장할 변수
            for i in range (8):     #delta로 주변 8방향 순회
                nr, nc = r + dr[i], c + dc[i]
                if nr in range(N) and nc in range(M):
                    if arr[nr][nc] < arr[r][c]:
                        cnt += 1
            if 4 <= cnt: #높이가 낮은 곳이 4개 이상
                ans += 1

    print(f'#{tc} {ans}')