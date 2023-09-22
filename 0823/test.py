#num = 0xA2
#print(bin(num)) #이진수로 출력
#0b10100010 - 0b가 붙고 앞의 0이 생략된다
#원래 1010 0010
#문제의 취지는 내장함수를 쓰지 않고 해결하는 것...
target = '41DA16CD' #0100 0111 1111 1110
# print(1//2) = 0
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



print(ans)
