def quick(aarray,low,high):
    if low>=high:
        return 0
    
    pivot=partition(aarray,low,high)
    quick(aarray,low,pivot)

    quick(aarray,pivot+1,high)

    return aarray
def partition(aarray,low,high):
    pivot=aarray[low]
    i=low-1
    j=high+1
   
    while True:
        i+=1
        while aarray[i]<pivot:
            i+=1
        j-=1
        while aarray[j]>pivot:
            j-=1
        if i>=j:
            return j
        else:
            aarray[i],aarray[j]=aarray[j],aarray[i]
            

aarray=[16, 4, 10, 14, 7, 9, 3, 2, 8, 1]

print(quick(aarray,0,len(aarray)-1))
