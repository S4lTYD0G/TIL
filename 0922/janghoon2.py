import sys
sys.stdin = open('janghoon_in.txt','r')
T = int(input())
#매개변수: 현재 레벨, 현재 탑의 높이
def recur(level, h_curr):
    global min_v
    #선반의 높이보다 탑의 높이가 높으면 return
    if h_shelf <= h_curr:
        min_v = min(min_v,h_curr)
        return

    # 종료 조건 :배열에 있는 수 다 더하면 끝
    if level == N:
        return

    # 해당 점원을 탑 쌓는데 사용할 경우
    recur(level+1, h_curr + arr[level])
    # 해당 점원을 탑 쌒는데 사용하지 않을 경우
    recur(level+1, h_curr)



for tc in range(1, T + 1):
    N, h_shelf = map(int, input().split())
    arr = list(map(int, input().split()))
    #visited 행렬을 만들고 이미 사용한 수를 판별한다

    #standard와 가장 차이가 적게 나는 수를 저장해 두기
    min_v= int(1e9)
    recur(0,0)
    print(f'#{tc} {min_v - h_shelf}')