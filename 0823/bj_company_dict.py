import sys
sys.stdin = open("bj_company_in.txt",'r')
N  = int(input())
employee = {}
curr = []
for _ in range(N):
    name, state = map(str, input().split())
    employee[name] = state

for key, items in employee.items():
    if items == "enter":
        curr.append(key)

curr.sort(reverse = True)
for people in curr:
    print(people)