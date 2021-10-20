def lomuto_quick_sort(array,low,high):
    if low >= high: # 원소가 1개인 경우
        return 
    pivot = lomuto_partition(array,low,high) 
    lomuto_quick_sort(array,low,pivot-1)
    lomuto_quick_sort(array,pivot+1,high)
    return array
def lomuto_partition(array,low,high):
    pivot = array[low]
    j = low 
    for i in range(low+1,high+1):
        if array[i] < pivot :
            j += 1 
            array[i],array[j] = array[j],array[i]     
    ##포지션 저장
    array[j],array[low] = array[low],array[j]
    return j

array=[1,23,4,5,6,78,9,10,111,123,45,6]

print(lomuto_quick_sort(array,0,len(array)-1))
