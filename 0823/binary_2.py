#비트 연산
val = 'F'
val = int(val, 16) #이정도는 int를 씁시다 
print(val)

ans = ''
num = '47FE'
ans += '1' if val & 8 else '0'
ans += '1' if val & 4 else '0'
ans += '1' if val & 2 else '0'
ans += '1' if val & 1 else '0'
print(ans)

for ch in num:
    if '0' <= ch <= '9':
        val = ord(ch) = ord('0')
    else:
        val = 10 + ord(ch) - ord('A')