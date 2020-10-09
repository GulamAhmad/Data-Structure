def selectionSort(A):  
    for i in range(len(A)): 
        small = i 
        for j in range(i+1, len(A)): 
            if A[small] > A[j]: 
                small = j 
        A[i], A[small] = A[small], A[i] 
  

#insertion sort
def insertionSort(arr): 

    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
  

#bubble sort
def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]
                

A = [64, 25, 12, 22, 11]   
opt = input("enter i,b or s for sorting")
if opt == 'i' :
    bubbleSort(A) 
    print("insertion sort")
    print(A)
elif opt == 'b':
    insertionSort(A)
    print ("bubblesort")
    print(A)
elif opt == 's':
    selectionSort(A)
    print ("selection sort") 
    print(A)
    


