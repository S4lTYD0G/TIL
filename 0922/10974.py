N = int(input())
#1부터 N까지 배열 만들기
arr = [i for i in range(1, N+1)]
visited = [0 for _ in range(N)]
picked = []
#안에 있는 숫자들 다 써야함 - visited 사용?
def recur(cnt):
    if cnt == N:
        print(*picked)
        return
    for i in range(N):
        if not visited[i]:
            picked.append(arr[i])
            visited[i] = 1
            recur(cnt + 1)
            visited[i] = 0
            picked.pop()

recur(0)