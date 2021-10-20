
def mergesplit(array):
    if len(array)<=1:
        return array
    mid=len(array)//2
    left=mergesplit(array[:mid])
    right=mergesplit(array[mid:])
    
    return merge(left,right)

def merge(left,right):
    i,j=0,0
    sort=[]
    
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            sort.append(left[i])
            i+=1
        else:
            sort.append(right[j])
            j+=1
    
    while i<len(left):   
        sort.append(left[i])
        i+=1
    
    while j<len(right):   
        sort.append(right[j])
        j+=1
        
    return sort


a = [1,23,4,5,6,78,9,10,111,123,45,6]
print("before sort : ",a)
print("after sort : ",mergesplit(a))

