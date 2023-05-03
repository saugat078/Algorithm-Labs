def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        #splitting array into two halves
        left_half = arr[:mid] 
        right_half = arr[mid:]

        #recursively calling merge sort on left and right halves
        merge_sort(left_half)
        merge_sort(right_half)

        merge(arr, left_half, right_half) #merging the splitted arrays into one
    return arr  
#merge step
def merge(arr, left_half, right_half):
    i = 0
    j = 0
    k = 0
    #compare left and right half elements and insert smaller one into the array
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1
    #inserting remaining element from left half into array
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1
    #inserting remaining element from right half into array
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1
    

my_array = [10,20,18,16,25,30]
merge_sort(my_array)
print(my_array) 