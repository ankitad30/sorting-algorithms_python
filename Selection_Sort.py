#Selction Sort


def selection_sort(A):

    for i in range(0, len(A) -1):   #last element is anyway be at apt position
        imin = i

        for j in range(i+1, len(A)):
            if A[j] < A[imin]:
                imin = j


        A[i], A[imin] = A[imin], A[i]



A= [54,26,93,17,77,31,44,55,20]
selection_sort(A)
print(A)




        
        
