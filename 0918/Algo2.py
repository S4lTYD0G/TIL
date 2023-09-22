#C 언어적 표현
arr = [69, 30, 10, 2, 16, 8, 32, 21]
# 정렬하려는 배열과 똑같은 크기의 배열 생성
tmp = [0] * len(arr)
def merge_sort(s,e):
    print(s, e)
    if s == e : return

    mid = (s + e) // 2
    merge_sort(s, mid)
    merge_sort(mid + 1, e)
    pass
result = merge_sort(0,len(arr)-1)
print(result)