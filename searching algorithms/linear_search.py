def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr=[1,7,8,4,9]
z=linear_search(arr,8)
print(z)