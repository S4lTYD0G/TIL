arr = list(map(int, input()))
if sum(arr) % 3 != 0 :
    ans = -1
else:
    arr.sort(reverse = True)
    if arr[-1] != 0:
        ans = -1
    else:
        ans = ''.join(map(str, arr))
        ans = int(ans)
print(ans)
