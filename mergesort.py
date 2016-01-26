# MERGESORT


def mergesort(A):

    if len(A) >1:
        mid= len(A)//2

        L= A[:mid]
        R= A[mid:]

        mergesort(L)
        mergesort(R)

        i=0
        j=0
        k=0


        while i< len(L) and j< len(R):
            if L[i]< R[j]:
                A[k]= L[i]
                i+=1
            else:
                A[k]=R[j]
                j+=1

            k+=1



# for left overs in either L or R

        while i < len(L):
            A[k]= L[i]
            i+=1
            k+=1

        while j< len(R):
            A[k]= R[j]
            j+=1
            k+=1

            
            

A= [54,26,93,17,77,31,445,55,20]
print(A)

mergesort(A)
print("The sorted array is : ", A)




            
                
