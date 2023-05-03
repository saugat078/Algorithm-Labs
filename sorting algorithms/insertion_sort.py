def insertion_sort(arr):
    #loop start from second element
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements in the sorted subarray that are greater than the current element one position to the right
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        #insert current element into correct position in sorted array
        arr[j + 1] = key
    return arr

array=[10,20,18,16,25,30]
z=insertion_sort(array)
print(z)