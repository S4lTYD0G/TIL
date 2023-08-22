import sys
sys.stdin = open('swea_hip_in.txt','r')
T = int(input())

def push(item):
    #완전 이진 트리 구조를 유지하기 위해 마지막 노드로 추가
    global last
    last += 1
    H[last] = item
    #부모 자식 간 대소 관계를 유지하도록 재조정
    p,c = last//2, last
    while p > 0 and H[p] > H[c]:
        H[p] , H[c] = H[c], H[p]
        c = p
        p = c//2

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    #저장소
    H = [0] * (N+1)
    last = 0

    for val in arr:
        push(val)

    sum = H[1]
    p = N//2
    while 1 < p:
        sum += H[p]
        p = p//2
    print(f'#{tc} {sum}')

