def merge_sort(input, start, end):
    print(input)
    mid = int((start + end) / 2)
    if start < end:
        merge_sort(input, start, mid)
        merge_sort(input, mid + 1, end)
    
    i = 0
    first = start
    last = mid + 1
    tmp = []
    while first <= mid and last <= end:
        if input[first] < input[last]:
            tmp.append(input[first])
            first += 1
        else:
            tmp.append(input[last])
            last += 1
        i += 1
    while first <= mid:
        tmp.append(input[first])
        first += 1
        i += 1
    while last <= end:
        tmp.append(input[last])
        last += 1
        i += 1

    i = 0
    while start <= end:
        input[start] = tmp[i]
        i += 1
        start += 1
    print(input)

input = [9,7,5,3,1,0,2,4,6,8]
print(input)
merge_sort(input, 0, 9)
print(input)
    