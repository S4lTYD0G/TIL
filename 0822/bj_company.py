import sys
sys.stdin = open('bj_company.txt','r')
N = int(input())
curr = []
for i in range(N):
    name, state = map(str, input().split())
    if state == "enter":
        curr.append(name)
    print(curr)