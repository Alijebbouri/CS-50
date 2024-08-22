def binary_search(num):
    arr = [1,2,3,4,5,6,7,8,9,10,11,12]
    start = 0
    end = len(arr) - 1
    while start <= end :
        mid = (start + end) // 2
        if arr[mid] == num:
            return mid
        elif arr[mid] < num:
            start = mid + 1
        else :
            end = mid - 1
    return 'not found'
print(binary_search(4))
        
            
            
        
        
        
            