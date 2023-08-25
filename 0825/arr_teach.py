N = 5
arr = [i for i in range(N)]
#2 구간으로 나누면 N-1 개의 나눌 수 있는 point가 있다
for i in range(1, N):
    pass
    #print(arr[:i],arr[i:])
    #slicing에서 시작과 끝을 표현하는 방식은 range와 동일

# 3구간으로 나누기

for i in range(1, N - 1): # i : 1 ~ N - 2
    for j in range (i + 1, N):  #j : i + 1 ~ N
        print(arr[:i], arr[i:j], arr[j:])
3