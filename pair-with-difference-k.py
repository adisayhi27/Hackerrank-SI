def diffOfPairs(ar,n):
    ar.sort()
    p1=0
    p2=0
    while(p2<n):
        if (ar[p2]-ar[p1]==k):
            return 'true'
        if (ar[p2]-ar[p1]>k):
            p1+=1
        else:
            p2+=1
          #  p2-=1
    return 'false'


m=int(input())
for i in range(m):
    n,k=map(int,input().split())
    ar=list(map(int, input().split()))[:n]
    print(diffOfPairs(ar,n))
