arr = [0, 1, 2, 3, 4]
N = len(arr)

for i in range(N - 2):
    num1 = 0
    for a in range(i + 1):
        num1 += arr[a]
    for j in range(i + 1, N - 1):
        num2 = 0
        num3 = 0
        for b in range(i + 1, j + 1):
            num2 += arr[b]
        for c in range(j + 1, N):
            num3 += arr[c]

        lst = [num1, num2, num3]