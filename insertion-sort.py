def insertionSort(arr): 
    for i in range(1, len(arr)):
        key = arr[i] 
        j = i-1
        while j >=0 and key < arr[j] : 
            arr[j+1] = arr[j] 
            j -= 1
        print(j+1, end=" ")
        arr[j+1] = key
    print()



n = int(input())
for k in range(n):
    m=int(input())
    arr=list(map(int,input().split()))[:m]
    insertionSort(arr)
