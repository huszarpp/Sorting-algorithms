def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j >= 1 and array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1 
        i += 1
    return array

array = [9,7,5,3,1,0,2,4,6,8]
print(insertion_sort(array))
