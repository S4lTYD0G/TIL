arr = list(input())
N = len(arr)
max_v = -1
picked = ''
visited = [0 for _ in range(N)]
def backtrack(cnt):
    global picked, max_v

    if cnt == N:
        picked_num = int(''.join(picked))
        if picked_num % 30 != 0:
            return
        if max_v < picked_num:
            max_v = picked_num
        return
    for i in range(N):
        if not visited[i]:
            picked += arr[i]
            visited[i] = 1
            backtrack(cnt+1)
            visited[i] = 0
            picked = picked[:-1]
backtrack(0)
print(max_v)