import sys
sys.stdin = open('calculator_in.txt','r')
from collections import deque
sum_lst = []
# 주어지는 숫자의 수
N = int(input())
# 숫자를 저장할 리스트
num_q = deque(map(int, input().split()))
#+, -, *, /
#순열 반환
def perm(k, n):
    if k == n:      #n이 arr 길이만큼 돌았으면
        print(test)
        while 1 < len(num_q):
            for i in range(len(test)):
                num1 = num_q.popleft()
                num2 = num_q.popleft()
                cal = test[i]
                if cal == '+':
                    sum = num1 + num2
                elif cal == "-":
                    sum = num1 - num2
                elif cal == "*":
                    sum = num1 * num2
                else:
                    sum = num1 // num2
                num_q.appendleft(sum)
            sum_lst.append(sum)
        return

    for i in range(k, n):
        test[i],test[k] = test[k],test[i]
        perm(k + 1, n)
        test[i],test[k] = test[k],test[i]


#정수 나눗셈(몫만 취함), 연산자 우선순위 무시하고 입력된 순서대로
#주어진 연산 순서
cal = list(map(int, input().split()))
cal_lst = ['+','-','*','/']
test = deque()
for n in range(4):
    if cal_lst[n] * cal[n] != '': #false가 아니면
        test.append(cal_lst[n] * cal[n])
perm(0, len(test))

print(sum_lst)


