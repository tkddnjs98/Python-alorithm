def binary (array,left,right,value):
    if left>right:
        return -1
    else:
        mid=(left+right)//2
        if a[mid]==value:
            return mid
        elif (a[mid]>value):
            return binary(array,left,mid-1,value)
        else:
            return binary(array,mid+1,right,value)

a=[1,2,3,5,6,7,5]
print(binary(a,0,len(a)-1,5))
