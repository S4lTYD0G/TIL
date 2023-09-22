arr = [69, 30, 10, 2, 16, 8, 32, 21]
def merge_sort(lst):
    print(lst)
    if len(lst) == 1:
        return lst
    else:
        #분할 하기
        mid = len(lst) // 2
        l =merge_sort(lst[:mid]) #왼쪽 반 뽑아옴
        r = merge_sort(lst[mid:]) #오른쪽 반 뽑아옴
        #l,r 을 병합해서 반환
        result = []
        while l and r:
            if l[0] < r[0]:
                result.append(l.pop(0))
            else:
                result.append(r.pop(0))
        #왼쪽이 남아있으면
        #여러개 있으면 한번에 때려박음
        if l:
            result.extend(l)
        if r:
            result.extend(r)
        #굳이 if문 쓸 필요 없음: 빈 리스트는 extemd 해도 변화 없음
        return result
        #멈추는 조건: 더 이상 나눌 수 없을만큼 작아졌을 때

result = merge_sort(arr)
print(result)