#{1,2,3,4,5,6,7,8,9,10}의 powerset 중 원소의 합이 10인 부분집합을 모두 출력
#sum이 10 이상이면 return
#이 문제를 다른 사람한테 완벽하게 설명할 수 있을 정도로!
arr = [i for i in range(1,11)]
path = []
def dfs(cnt):
    if sum(path) == 10:
        print(*path)
        return
    for num in arr:
        #가지치기
        if sum(path) > 10 or num in path:
            continue
        path.append(arr[cnt])
        dfs(cnt + 1)
        path.pop()

dfs(0)

