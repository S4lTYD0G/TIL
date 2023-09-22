import sys
sys.stdin = open('tree_in.txt','r')
V, E = map(int, input().split())
arr = list(map(int, input().split()))

L = [0] * (V + 1) #왼쪽 자식 저장
R = [0] * (V + 1) #오른쪽 자식 저장
P = [0] * (V + 1) #부모의 번호 저장
#0은 가리키는 게 없다.

# ===========트리 저장 ================
for i in range(0, len(arr), 2):
    p, c = arr[i], arr[i + 1]
    #왼쪽 자식을 확인
    if L[p] == 0:
        L[p] = c
    else: #값이 있으면. 오른쪽에 자식 저장
        R[p] = c

    #c의 부모는 P[c]에
    P[c] = p

# ================================순회
def dfs(v):
    if v == 0 :
        return
    #언제 끊지?
    #단말 node - 자식이 없는 node를 만났을 때
    #단말 node 이면 0이 넘어간다
    #print(v, end = ' ')
    dfs(L[v])
    #왼쪽 자식에서 귀환
    print(v, end=' ') #중위순회
    dfs(R[v])
    #print(v, end=' ')
#3번씩 연달아 숫자가 나오는 곳은 단말 노드
dfs(6)
#트리는 방문 정보를 쓸 필요가 없다
# 사이클이 없고 부모에서 자식 방향으로 가기 때문