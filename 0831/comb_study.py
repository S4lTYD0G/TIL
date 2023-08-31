arr = "ABCDE"
pick = []
n = len(arr)
r = 3

def comb(n, r, start):
    if r == 0:
        print(pick)
        return

    for i in range(start, n - r + 1):
    # for i in range(start, n):
        pick.append(arr[i])
        comb(n, r - 1, i + 1)
        pick.pop()

comb(n, r, 0)
