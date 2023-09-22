import sys
sys.stdin = open('binary_in.txt','r')
T = int(input())
for tc in range(1, T+1):
    len_target, target = map(str, input().split())
    over_ten = {'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
    ans = ''
    for num in target:
        if num.isdigit():
            num = int(num)
            lst = []
            while 0 < num: #몫이 0이 될 때까지
                lst.append(num % 2)
                num = num // 2
                #몫(0)을 더해준다
                #더해주고 나면 뒤집어야 함
            if len(lst) < 4:
                while len(lst) < 4:
                    lst.append(num//2)
            lst = lst[::-1]
            ans += ''.join(list(map(str, lst)))
        else: #10 넘으면(알파벳이면)
            ans += over_ten[num]



    print(f'#{tc} {ans}')