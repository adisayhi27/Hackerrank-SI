def bubble(ar,n):
    count=0
    for i in range(n):
        for j in range(0,n-i-1):
            if ar[j]>ar[j+1]:
                ar[j], ar[j+1] = ar[j+1], ar[j]
                count+=1
    print(count)

m = int(input())
for k in range(m):
    n = int(input())
    ar=list(map(int, input().split()))[:n]
    bubble(ar,n)
