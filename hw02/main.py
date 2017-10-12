def bsearch(data, target):
    
    left=0
    right=len(data)-1
    while left <= right:
        mid = (left+right)// 2;  
        if target == data[mid]:  
            return mid
        elif target < data[mid]:  
            right=mid-1
        elif target > data[mid]:
            left=mid+1 
    else:
        return None;  
count=[3,7,9,11,15,23,25]
en=bsearch(count,11)
print(en)
