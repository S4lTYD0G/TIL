import sys
sys.stdin = open("R_flag_in.txt",'r')
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split()) #행, 열

    # 하나씩 떼어서 입력 받기
    arr = [list(input()) for _ in range(N)]

    #임의 최솟값
    min_cnt = 99999999

    #흰색 - 파란색 경계 i, 파란색- 빨간색 경계 j
    for i in range(1, N-1):
        for j in range(2, N):
            cnt = 0

            #흰색 영역
            for r in range(0, i):
                for c in range(0, M):
                    if arr[r][c] != "W":
                        cnt += 1

            #푸른색 영역
            for r in range(i, j):
                for c in range(0, M):
                    if arr[r][c] != "B":
                        cnt += 1

            #붉은색 영역
            for r in range(j, N):
                for c in range(0, M):
                    if arr[r][c] != "R":
                        cnt += 1

        # 출력 - rectangle 들과 같은 줄로 맞추기
            #for line in arr:
                #print(line)

            if cnt < min_cnt:
                min_cnt = cnt
            #print('==================')
    print(f'#{tc} {min_cnt}')