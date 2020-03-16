def elementDistinct(ar,n,k):
    mydict = {}
    cnt=0
    for i in range(k):
        try:
            if mydict[ar[i]] != 0:
                mydict[ar[i]] += 1
                #cnt+=1
        except KeyError:
            mydict[ar[i]] = 1
            cnt += 1

    print(cnt, end=' ')

    for i in range(k,n):
        if mydict[ar[i-k]]==1:
            cnt -=1
            del mydict[ar[i-k]]
        else:
            mydict[ar[i-k]]-=1

        try:
            if mydict[ar[i]]!=0:
                mydict[ar[i]] += 1
        except KeyError:
            mydict[ar[i]] = 1
            cnt += 1

        print(cnt, end=' ')

m=int(input())
for i in range(m):
    n,k=input().split()
    n=int(n)
    k=int(k)
    ar=list(map(int, input().split()))[:n]
    elementDistinct(ar,n,k)
    print()
