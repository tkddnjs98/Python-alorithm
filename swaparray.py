def swaparray(array,low,high):
    i=low
    j=high
    if i>=j:
        return array
    else:
        array[i],array[j]=array[j],array[i]
        return swaparray(array,low+1,high-1)
array=["c","h","i","c","k","e","n"]

print(swaparray(array,0,len(array)-1))
