import math

def mergeSort(nlist):
    print("Splitting ",nlist)
    # insert your code to complete the mergeSort function
    point1 = 0
    point2 = len(nlist)
    midPoint = math.floor(point2 / 2)
    firstHalf = nlist[point1: midPoint]
    secondHalf =nlist[midPoint: point2]
    if len(nlist)-1 > 0:
        mergeSort(firstHalf)
        mergeSort(secondHalf)
    merge(nlist, firstHalf, secondHalf)
    
    print("Merging ",nlist)
    return nlist

def merge(nlist,lefthalf,righthalf):
    i=j=k=0       
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            nlist[k]=lefthalf[i]
            i=i+1
        else:
            nlist[k]=righthalf[j]
            j=j+1
        k=k+1

    while i < len(lefthalf):
        nlist[k]=lefthalf[i]
        i=i+1
        k=k+1

    while j < len(righthalf):
        nlist[k]=righthalf[j]
        j=j+1
        k=k+1
    return nlist

num = [ 55 ,  31 ,  26 ,  20 ,  63 ,  7 ,  51 ,  74 ,  81 ,  40 ]
sorted = mergeSort(num)
print("Sorted: " , sorted)