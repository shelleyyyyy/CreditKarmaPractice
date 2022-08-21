
def contains(arr, k):    
    count = 0
    for i in arr:
        if i == k:
            count = count + 1
            

def find_unique(arr):
    for i in arr:
        if contains(arr, arr[i]) == 1:
            return arr[i]
        
    return False
            
        
            
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 21, 1, 3, 4, 5, 6, 7, 8, 9, 2]

print(find_unique(arr))
