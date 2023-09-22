import sys
sys.stdin = open('elec_bus_in.txt','r')
T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    #도착해야하는 정류장
    goal = arr[0]
    #각 정류장 충전기 용량
    capacity = arr[1:]
    min_change = 9999
    def backtrack(curr, bett, cnt): #현재 정류장 정보, 충전지 잔량, 충전 횟수
        if curr == goal: #현재 위치가 goal이면
            return cnt
        #베터리가 0이 아니면
        if bett != 0:
            #교체하고 이동
            backtrack(curr+1, capacity[curr], cnt+1)

    result = backtrack(1,capacity[0],0)
    print(result)

