
def quick_sort(A):
    quick_sort_ite(A,0,len(A)-1)

def quick_sort_ite(A, low, hi):
    temp_stack = []
    temp_stack.append((low,hi))
    
    #Main loop to pop and push items until stack is empty
    while temp_stack:      
        pos = temp_stack.pop()
        low = pos[0]
        hi = pos[1]
        p = partition(A,low,hi)
        #If items in the left of the pivot push them to the stack
        if p-1 > low:
            temp_stack.append((low,p-1))
        #If items in the right of the pivot push them to the stack
        if p+1 < hi:
            temp_stack.append((p+1,hi))
       

def get_pivot(A, low, hi):
    mid =(hi+low) // 2
    pivot = hi
    if A[low] < A[mid]:
        if A[mid] < A[hi]:
            pivot = mid
    elif A[low] < A[hi]:
            pivot = low
    return pivot

def partition(A, low, hi):
    pivotIndex = get_pivot(A, low, hi)
    pivotValue = A[pivotIndex]
    A[pivotIndex], A[low] =A[low], A[pivotIndex] 
    border = low

    for i in range(low, hi+1):
        if A[i] < pivotValue:
            border +=1
            A[i], A[border] =A[border], A[i]
    A[low],A[border] = A[border], A[low]

    return border
    
        
A = [7,2,1,6,8,5,3,4]
quick_sort(A)
print(A)
