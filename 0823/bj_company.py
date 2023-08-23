#넣었다 뺏다 하는 게 비효율적인가
from sys import stdin
N  = int(stdin.readline())
employee = []
for _ in range(N):
    name, state = map(str, stdin.readline().split())
    if state == "enter":
        employee.append(name)

    elif state == "leave":
        employee.remove(name)

employee.sort(reverse = True)
for person in employee:
    print(person)

