#Bubble sort


def bubblesort(A):

  for k in range(1, len(A)):
       flag =0      
       for i in range(0, len(A) -1):   #to avoid going through sorted array again and to avoid swapping so set flag
           
            if A[i]> A[i+1]:
                
                A[i], A[i+1]= A[i+1], A[i]

       if(flag==0): break         
                



A = [54, 26, 93, 17, 77, 31, 445, 55, 20]
bubblesort(A)
print(A)
