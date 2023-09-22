nums = [1, 2, 3, 4, 5]
N = len(nums)
ans = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        nums[i], nums[j]  = nums[j], nums[i]
        val = int(''.join(map(str, nums)))
        print(val)
        nums[i], nums[j] = nums[j], nums[i]