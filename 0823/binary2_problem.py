import sys
sys.stdin = open('binary_2_in.txt','r')
T = int(input())
for tc in range(1, T+1):
    num = float(input())
    binary_num = [] #정답 저장을 위한 배열

    flag = 1 #소숫점 아래 12자리가 넘는지 여부를 판단하기 위한 flag 변수
    while True: #소수를 이진수로 바꾸는 방법 이용
        num *= 2
        if 1 <=  num:
            num -= 1
            binary_num.append(1)
        elif 0 < num < 1:
            binary_num.append(0)
        if int(num) == num: #소숫점 아래 수가 0이 될 때까지
            break
        if 12 < len(binary_num):
            flag = 0
            break
    if flag:
        ans = ''.join(list(map(str,binary_num)))
        print(f'#{tc} {ans}')
    else:
        print(f'#{tc} overflow')



