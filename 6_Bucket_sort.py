import math

def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j >= 1 and array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1 
        i += 1
    return array

def bucket_sort(array, k):
    buckets = []
    max_val = max(array)
    for i in range(k):
        buckets.append([])
    for num in array:
        buckets[math.floor(num * k / (max_val + 1))].append(num)
    for i in range(len(buckets)):
        buckets[i] = insertion_sort(buckets[i])
    result = []
    for bucket in buckets:
        result += bucket
    return result

array = [49,23,11,22,33,44]
print(bucket_sort(array, 5))