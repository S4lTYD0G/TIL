import sys
sys.stdin = open('janghoon_in.txt','r')
T = int(input())
def backtrack(cnt ,sum_height):
    global min_diff
    #print(sum_height)

    diff =  sum_height - standard
    if diff > 0:
        if diff < min_diff:
            min_diff = diff
        return

    for i in range(length):
        if visited[i]:
            continue
        else:
            sum_height += arr[i]
            visited[i] = 1
            backtrack(cnt + 1 , sum_height)
            sum_height -= arr[i]
            visited[i] = 0


for tc in range(1, T + 1):
    N, standard = map(int, input().split())
    arr = list(map(int, input().split()))
    length = len(arr)
    #visited 행렬을 만들고 이미 사용한 수를 판별한다
    visited = [0 for _ in range(length)]
    #standard와 가장 차이가 적게 나는 수를 저장해 두기
    #배열에 있는 수 다 더하면 끝
    min_diff = 0xfffffffffff
    backtrack(0,0)
    print(f'#{min_diff}')

