

def remove_evens(arr):
    for x in arr:
        if(x % 2 == 0):
            arr.remove(x)
            
            
    return arr


arr = [0, 1, 2, 3, 4, 5, 6, 7]

arr = remove_evens(arr)

print(arr)
            
            
