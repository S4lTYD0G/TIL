import sys
sys.stdin = open('vertical_talk.txt','r')
T = int(input())
for tc in range(1, T + 1):
    arr = []
    max_len = -1
    # 배열 입력 받기
    # 입력 받으며 가장 긴 list의 길이 찾기
    for _ in range(5):
        lst = list(input())
        arr.append(lst)
        if max_len <= len(lst):
            max_len = len(lst)

    #최종 행렬
    result_lst = [['*'] * max_len for _ in range(5)]
    #최종 행렬에 기본 행렬 요소 하나씩 넣기
    k = 0
    for lst in arr:
        for i in range(len(lst)):
            result_lst[k][i] = lst[i]
        k += 1
    #정답 저장을 위한 str
    ans = ''
    #최종 행렬 행 우선 순회
    for c in range(max_len):
        for r in range(5):
            ans += result_lst[r][c]

    ans = ans.replace('*','') #replace = 반환값 받아줘야 함
    print(f'#{tc} {ans}')


