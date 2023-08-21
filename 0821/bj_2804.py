A, B = map(str, input().split())
arr = [list('.' * len(A))for _ in range(len(B))]
flag = 1
for s_a in A:
    if flag ==0:
        break
    for s_b in B:
        if s_a == s_b:
            comm_s = s_a
            flag = 0

verti = A.index(comm_s) #A의 공통 문자는 세로 문자의 위치(열)을 결정
horri = B.index(comm_s) #B의 공통 문자는 가로 문자의 위치(행)을 결정

for i in range(len(A)):
    arr[horri][i] = A[i]

for j in range(len(B)):
    arr[j][verti] = B[j]

for line in arr:
    print(''.join(line))