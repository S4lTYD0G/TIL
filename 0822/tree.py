tree = [0, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', "J"]
#이진 탐색 트리 : 탐색을 효율적으로 하기 위해 사용...
#이진 검색은 정렬이 되어 있어야 검색가능?

def inorder(v): #노드 번호 = 인덱스
    if v > N:
        return
    print(tree[v], end ='  ')
    inorder(v*2) #왼쪽
    #tree[v] = num
    #num += 1
    inorder(v*2 +1) #오른쪽

N = 10
inorder(1)
#print(tree)