#n번 정류장까지 가는 데 필요한 최소 베터리 교환 횟수
def charge(n):
    #기저 사례
    #교체횟수 0으로 도달할 수 있는 거리
    if n <= 1 + arr[1]:
        return 0
    #일반 사례
    for i in range(1, n):
        if