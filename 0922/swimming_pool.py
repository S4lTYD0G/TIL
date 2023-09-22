#1일. 한달, 세달, 1년
# 금액이 최소인 것
# 계산 중간에 가격이 넘어가면 가지치기...
import sys
sys.stdin = open('swimming_pool_in.txt','r')
#넘겨줘야 하는 것: 현재 달(cnt), 현재 요금
def recur(cnt, curr_fee):
    global min_fee
    #가지치기
    if min_fee < curr_fee:
        return

    #cnt = 배열 인덱스라서 0부터 시작. 달로 맞추려면 +1 해줘야
    if 12 < (cnt + 1):
        #부등호 넣으면 안됨!!!!
        min_fee = min(min_fee, curr_fee)
        return
    #일일 이용권 선택
    recur(cnt+1, curr_fee + (month[cnt] * p_day))
    #월 이용권 선택
    recur(cnt+1, curr_fee + p_mth)
    # 3달 이용권 선택
    recur(cnt+3, curr_fee + p_3mth)
    # 1년 이용권 선택
    recur(cnt+12, curr_fee + p_year)



T = int(input())
for tc in range(1, T+1):
    p_day, p_mth, p_3mth, p_year = map(int, input().split())
    month = list(map(int, input().split()))
    min_fee = int(1e9)

    recur(0,0)
    print(f'#{tc} {min_fee}')
'''
재귀 
1일, 한달 이용권 선택 > 다음 달로 넘긴다
3달 이용권 선택 > 3달 뒤로 넘긴다
1년 이용권 선택> 12달 뒤로 넘긴다

month가 12이상이면 함수를 종료한다. 
'''

