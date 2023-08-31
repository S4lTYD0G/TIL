import sys
sys.stdin = open('dock_in.txt','r')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    dock_time = []
    for i in range(N):
        start, end = map(int, input().split())
        dock_time.append((start, end))



    for n in range(len(dock_time)):
        sorted_dock = sorted(dock_time, key = lambda x : dock_time[n][1])
    print(dock_time)
    print(sorted_dock)