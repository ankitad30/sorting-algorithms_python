def swap(i, j):
    h_list[i], h_list[j] = h_list[j], h_list[i]

def heapify(end,i):   #creates a tree with parent and 2 child nodes
    l=2 * i  
    r=2 * i + 1   
    max=i   
    if l < end and h_list[i] < h_list[l]:   
        max = l   
    if r < end and h_list[max] < h_list[r]:   
        max = r   
    if max != i:   
        swap(i, max)   
        heapify(end, max)   

def heap_sort():     
    end = len(h_list)                
    start = end / 2 - 1              # working way up in the heap, one small tree with 1parent and children
    for i in range(start, -1, -1):   #reversal from start till -1 not inclusive of -1
        heapify(end, i)   
    for i in range(end-1, 0, -1):   # from end-1 till 0(not inclusive)in increments of -1
        swap(i, 0)   
        heapify(i, 0)   

h_list = [2, 7, 1, -2, 56, 5, 3]
heap_sort()
print(h_list)
