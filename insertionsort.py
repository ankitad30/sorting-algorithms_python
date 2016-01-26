#insertion sort


def insertionsort(A):
    for index in range(1, len(A)):


      currentvalue= A[index]
      position = index

      while position>0 and A[position-1]>currentvalue:
           A[position]= A[position-1]
           position =position-1

      A[position] = currentvalue


A= [9,3,6,4]
insertionsort(A)
print(A)


    
