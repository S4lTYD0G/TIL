import sys
sys.stdin = open('bj_8979_in.txt','r')
N, target = map(int, input().split())
score =  [0] * (N)
rank = [0] * (N)
#메달 수를 점수로 바꾸기
for _ in range(N):
    num_list = list(map(str, input().split()))
    idx = int(num_list.pop(0))
    dex_num = int(''.join(num_list))
    score[idx-1] = dex_num

print(score)
#rank 결정하기
score_sorted = sorted(score, reverse = True)
print(score_sorted)
