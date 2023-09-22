num = input()
ori_num = num
cnt = 0
sum = 0

if len(num) < 2:
    num = num * 2
    mod_num = num

while True:
    for s in num:
        sum += int(s)
    sum = str(sum)
    new_num = num[-1] + sum[-1]
    cnt += 1
    if 2 <= len(ori_num): #주어진 숫자가 한자리 수가 아닐 때
        if new_num == ori_num:
            break
    else: #주어진 수가 한자리 수일 때
        if new_num == mod_num:
            break
    num = new_num
    sum = 0

print(cnt)