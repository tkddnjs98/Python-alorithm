def pel(array,low,high):
    i=low
    j=high
    if i>=j:
        return 1
    elif array[i]!=array[j]:
        return -1
    else: return pel(array,low+1,high-1)


array="abcba"

print(pel(array,0,len(array)-1))
