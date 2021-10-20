import copy
import sys
sys.setrecursionlimit(100000)
#input = sys.stdin.readline

def quick_sort(array,low,high):
    if low >= high: # 원소가 1개인 경우
        return 
    else:
        pivot = hoare_partition(array,low,high) 
        quick_sort(array,low,pivot)
        quick_sort(array,pivot+1,high)
        return array
def hoare_partition(array,low,high):
    pivot = array[low]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while array[i] < pivot:
            i += 1
        j-=1
        while array[j] > pivot :
            j -= 1
        if i>=j : # 만일 두 인덱스가 겹쳤다면
            return j
        else:
            array[i],array[j] = array[j],array[i]



array=[16, 4, 10, 14, 7, 9, 3, 2, 8, 1]

print(quick_sort(array,0,len(array)-1))
