import sys
sys.stdin = open('switch_in.txt','r')
N = int(input())
arr = list(map(int, input().split()))
num_student = int(input())
for iter in range(num_student):
    gender, key = map(int, input().split())
    if gender == 1: #남학생일 때:
        for num in range(key-1, N, key): #범위 주의
            if arr[num] == 1:
                arr[num] = 0
            else:
                arr[num] = 1

    elif gender == 2 : #여학생일 때
        #key에 해당하는 값 바꾸기
        arr[key -1] = abs(arr[key-1] -1) #0이면 1, 1이면 0
        i = 1
        while True:
            pre = (key - 1) - i
            post = (key - 1) + i
            if pre < 0 or (N-1) < post: #pre, post가 범위 넘어가면
                break
            elif arr[pre] != arr[post]:
                break
            arr[pre] = arr[post] = abs(arr[pre]-1)
            i += 1

    else:
        break

#출력
divide = num_student // 20

if divide > 0:
    idx = 0
    for i in range(divide):
        print(*arr[i: i + 20])
        idx += 1
    print(*arr[idx * 20:])
else:
    print(*arr)


