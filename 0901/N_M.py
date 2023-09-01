N  = 4
M = 3
arr = [i for i in range(1, N + 1)]
stack = []
cnt = 0
pick = []
def dfs(arr):
    global cnt
    if len(stack) == M :
        print(*stack)
        return
    else:
        for num in arr:
            if num not in stack:
                stack.append(num)
                dfs(arr)
                stack.pop()
dfs(arr)


