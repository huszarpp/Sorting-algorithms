def counting_sort(array, k):
    output = array
    counter = [0] * k

    for num in array:
        counter[num] += 1
    
    ndx = 0 
    for i in range(len(counter)):
        while counter[i] > 0:
            output[ndx] = i
            counter[i] -= 1
            ndx += 1

    return output

print(counting_sort([1,4,1,2,7,5,2], 10))
