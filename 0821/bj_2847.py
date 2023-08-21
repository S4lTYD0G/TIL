N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
cnt = 0
while 1 < len(arr):
    if arr[-1] == max(arr) and arr[-2] != arr[-1]:
        arr.pop()
    elif arr[-2] < arr[-1]:
        arr.pop()
    else:
        arr[-2] -= 1
        cnt += 1

print(cnt)