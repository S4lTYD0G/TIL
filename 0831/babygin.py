import sys
sys.stdin = open('babyjin_in.txt')

def triplet(player):
    card_list = list(set(player))  # 중복 없이 p1이 가진 카드 종류 반환
    for i in range(len(card_list)):
        cnt = player.count(card_list[i])
        if cnt == 3:
            return 1
    return 0

def runs(player):
    card_list = list(set(player)) #set으로 중복 제거 안 할 경우 1, 2, 2, 3... 등 못 잡아냄
    card_list.sort() #오른차순 정렬
    for i in range(len(card_list) - 2):
        if card_list[i + 1] == card_list[i] + 1 and card_list[i + 2] == card_list[i] + 2:
            return 1
    return 0

T = int(input())
for tc in range(1, T+1):
    card = list(map(int, input().split()))
    ans = 0
    p1 = []
    p2 = []

    for i in range(len(card)):
        if i % 2 == 0 :
            p1.append(card[i])
        else:
            p2.append(card[i])
        if 5 <= i: #p1, p2 이 가진 카드 수가 각각 3장 이상일 때
            if triplet(p1) == 1 or runs(p1) == 1:
                ans = 1
                break
            elif triplet(p2) == 1 or runs(p2) == 1:
                ans = 2
                break

    print(f'#{tc} {ans}')