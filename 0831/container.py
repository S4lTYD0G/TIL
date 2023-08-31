import sys
from collections import deque
sys.stdin = open('container_in.txt','r')
T = int(input())
for tc in range(1, T + 1):
    ct, truck = map(int,input().split()) #컨테이너, 트럭 수
    ct_w = list(map(int, input().split())) #컨테이너 무게
    truck_max_w = list(map(int, input().split())) #트럭 적재용량

    ct_w.sort(reverse= True)
    truck_max_w.sort(reverse = True)

    head = 0 #ct 인덱스 접근
    ans = 0 #정답 저장

    for i in range(truck):
        if ct_w[head] <= truck_max_w[i]: #컨테이너 무게가 트럭 적재용량보다 작거나 같으면
            ans += ct_w[head]
            head += 1
        else: #트럭 고정(for문 돌고 있음), 컨테이너를 담을 수 있는 크기의 트럭이 나타날 때까지
            while truck_max_w[i] < ct_w[head]:
                head += 1
                if head == ct:
                    break

    print(f'#{tc} {ans}')