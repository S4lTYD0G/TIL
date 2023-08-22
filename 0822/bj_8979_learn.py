import sys
sys.stdin = open('bj_8979_in.txt','r')
N, k = map(int,input().split())
medals = [list(map(int, input().split())) for _ in range(N)]
medals.sort (key = lambda x: (x[1], x[2], x[3]), reverse = True) #우선순위
#print(medals)

for i in range(N):
    if medals[i][0] == k:
        idx = i #1

for i in range(N): #다시 0부터 순회
    if medals[idx][1:] == medals[i][1:]: #같은 값이 있으면
        print(i+1)
        break
