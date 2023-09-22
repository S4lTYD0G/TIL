import sys
sys.stdin = open('binary_cyper_in.txt','r')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) #행, 열
    arr = [list(input()) for _ in range(N)]
    cyper = []

    # 거꾸로 접근하여 1이 처음 등장하는 부분의 좌표 찾기
    for r in range(N):
        for c in range(M-1, -1, -1):
            if arr[r][c] == '1':
                start_r, start_c = r, c
                break
    # 암호 저장
    for i in range (start_c, start_c - 56, -1):
        cyper.append(arr[start_r][i])

    cyper = ''.join(cyper[::-1]) #거꾸로 접근하여 저장했으므로 뒤집기

    #암호의 원문을 저장하는 dict
    cyper_original = {
        '0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3,
        '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7,
        '0110111': 8, '0001011': 9
                    }
    cyper_num = []
    for i in range(8):
        cyper_num.append((cyper_original[cyper[ 7*i : 7*(i+1) ]]))
    #cyper[0 : 7] , cyper[7: 14] ... 에 접근하며 원문에 해당하는 key값 찾기

    even_num = 0 #짝수 번호 수의 합 저장
    odd_num = 0 #홀수 번호 수의 합 저장

    for i in range(8): #cyper 길이 : 8
        if i % 2 == 0: #짝수 번호:
            even_num += cyper_num[i]
        else:
            odd_num += cyper_num[i]

    result = even_num * 3 + odd_num

    if result % 10 == 0 : #정답이 조건을 만족하면
        print(f'#{tc} {sum(cyper_num)}')
    else:
        print(f'#{tc} 0')