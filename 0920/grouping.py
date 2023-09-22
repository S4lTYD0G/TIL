import sys
sys.stdin = open('grouping_in.txt','r')
T = int(input())
for tc in range(1, T + 1):
    #출석 번호(N), 신청서 수(M)
    N,M = map(int, input().split())
    #부모 저장소를 생성하면서 초기화
    p = [i for i in range(N+1)]

    #연산
    def find_set(x): #x가 속한 집합이 뭔지 알려줘!
        if x == p[x]:
            return x
        else:
            ret = find_set(p[x])
            p[x] = ret
        return p[x]

    def union(x,y): #x와 y가 속한 두 집합을 합친다.
        # 두 트리를 합친다 - 한 트리를 다른 트리의 서브 트리로 가져다 둔다
        a = find_set(x)
        b = find_set(y)
        #이미 같은 집합이면 못합쳐유
        if a == b: return

        p[b] = a #p[a] = b
        pass