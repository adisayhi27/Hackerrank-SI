def sumOfArray(ar,n):
    k=0
    for i in range(n):
       k=k+ar[i]
    print(k)


m=int(input())
for i in range(m):
    n = int(input())
    ar=list(map(int, input().split()))
    sumOfArray(ar,n)
