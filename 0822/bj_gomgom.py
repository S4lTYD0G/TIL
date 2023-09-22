import sys
sys.stdin = open('gomgom_in.txt','r')
from sys import stdin
from collections import deque

N = int(stdin.readline())
arr = deque()
for i in range(N):
    arr.append(stdin.readline().strip())

sum = 0
while arr:
    s_lst = []
    if arr.popleft() == "ENTER":
        while arr and arr[0] != "ENTER": #while arr 안하면 idx out of range error 남
            s_lst.append(arr.popleft())
        s_lst = set(s_lst)
        sum += len(s_lst)

print(sum)