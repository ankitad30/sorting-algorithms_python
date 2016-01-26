#QUICKSORT


def quicksort(A):
    quicksort2(A, 0, len(A) -1)


def quicksort2(A, low, hi):
    if low < hi:   # exits if segment is invalid and segment has one value
        
         p = partition(A, low, hi)
         quicksort2(A, low, p-1)
         quicksort2(A, p+1, hi)


def get_pivot(A, low, hi):

    mid = (hi+low) //2
    pivot = hi

    if A[low]<A[mid]:
        if A[mid]< A[hi]:
             pivot = mid
    elif A[low] < A[hi]:
             pivot = low

    return pivot



def partition(A, low, hi):

    pIndex = get_pivot(A,low,hi)
    pivotValue = A[pIndex]

    A[pIndex], A[low] = A[low], A[pIndex] 
    border = low

    for i in range(low, hi+1):
        if (A[i] < pivotValue):
            border +=1
            A[i], A[border]= A[border], A[i]

    A[low], A[border] = A[border], A[low]
    return border


A = [7,2,1,6,8,5,3,4]
print(A)
quicksort(A)
print("The sorted array is:", A)




            
