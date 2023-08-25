#구간합
arr = [0, 1, 2, 3, 4]
N = len(arr)

for split_1 in range(1, N-1): #N-2까지 갈 수 있음?
    sum_sec1 = 0
    for num1 in range(0,split_1):
        sum_sec1 += arr[num1]
        sum_sec2 = 0
        for num_2 in range(num1 +1, N-1):
            sum_sec2 += arr[num_2]
            sum_sec3 = 0
            for num_3 in range(num_2 + 1, N):
                sum_sec3 += arr[num_3]
            sum_lst = [sum_sec1, sum_sec2, sum_sec3]
            print(sum_lst)

