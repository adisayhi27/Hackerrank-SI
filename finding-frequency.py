## Using Binary Search recursive

from itertools import groupby

def findingFreq(ar,n,q_ar,m):
    ar=sorted(ar)
    ar_distinct=set(ar)
    ar_distinct = sorted(ar_distinct)
    ar_distinct_lst = list(ar_distinct)

    ar_distinct_cnt=[len(list(group)) for key, group in groupby(ar)]

    def BS(i, q, q_ar, m, ar_distinct_lst, lo, hi):
        mid = int((lo + hi) // 2)
        if (lo>=hi and q != ar_distinct_lst[mid]):
            return 'aditya'
        elif (q == ar_distinct_lst[mid]):
            return mid
        elif (ar_distinct_lst[mid] < q_ar[i]):
            return BS(i, q, q_ar, m, ar_distinct_lst, mid + 1, hi)
        else:
            return BS(i, q, q_ar, m, ar_distinct_lst, lo, mid)

    for i in range(m):
        lo=0; hi=len(ar_distinct_lst)-1
        q=q_ar[i]
        Qmid=BS(i,q,q_ar,m,ar_distinct_lst,lo,hi)
        if Qmid=='aditya':
            print(0)
        else:
            print(ar_distinct_cnt[Qmid])


n = int(input())
ar=list(map(int, input().split()))[:n]
m=int(input())
q_ar=[]
for i in range(m):
    q_ar.append(int(input()))
findingFreq(ar,n,q_ar,m)


#######################################################################################################

## Using BinarySearch1 and BinarySearch2

def findingFreq(ar,n,q_ar,m):
    ar_sorted=sorted(ar)

    def BS1(ar_sorted,n,x):
        p1=-1
        lo=0
        hi=n-1

        while(lo<=hi):
            mid=((lo+hi)//2)
            if(ar_sorted[mid]<x):
                lo=mid+1
            elif (ar_sorted[mid]>x):
                hi=mid-1
            else:
                p1=mid
                hi=mid-1
        return p1

    def BS2(ar_sorted,n,x):
        p2=-1
        lo=0
        hi=n-1

        while(lo<=hi):
            mid=((lo+hi)//2)
            if(ar_sorted[mid]<x):
                lo=mid+1
            elif (ar_sorted[mid]>x):
                hi=mid-1
            else:
                p2=mid
                lo=mid+1
        return p2

    for i in range(m):
        p1 = BS1(ar_sorted, n, q_ar[i])
        p2 = BS2(ar_sorted, n, q_ar[i])
        if (p1==-1 or p2==-1):
            print(0)
        else:
            print(p2 - p1 + 1)

n = int(input())
ar=list(map(int, input().split()))[:n]
m=int(input())
q_ar=[]
for i in range(m):
    q_ar.append(int(input()))
findingFreq(ar,n,q_ar,m)
