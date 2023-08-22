import sys
sys.stdin = open('blackjack_in.txt','r')

from itertools import permutations

min_abs = 1000000 #범위 신경 안쓰면 런타임 에러 난다... 
len_arr, key = map(int, input().split())
arr = list(map(int, input().split()))

for i in permutations(arr,3):
    #print(type(i)) #tuple로 반환됨
    curr_abs = abs(sum(i) - key)
    if curr_abs <= min_abs and sum(i) <= key :
        min_abs = curr_abs
        min_abs_num = sum(i)

print(min_abs_num)