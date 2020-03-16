import sys

def findfloor(ar_sorted,n,x):

    lo = 0
    hi = n - 1

    while (lo <= hi):
        mid = ((lo + hi) // 2)
        if (ar_sorted[mid]==x):
            return mid
        elif (ar_sorted[mid] < x and mid == n-1):
            return mid
        elif (ar_sorted[mid] < x and mid == 0):
            return mid
        elif ar_sorted[mid-1] <= x and ar_sorted[mid] > x:
            return mid-1
        elif (ar_sorted[mid] < x):
            lo = mid + 1
            #hi = mid - 1
        elif (ar_sorted[mid] > x):
            hi = mid - 1
            #lo = mid + 1
        #else:
         #   return sys.maxsize
    #return -1

n = int(input())
ar=list(map(int, input().split()))[:n]
ar_sorted = sorted(ar)
m=int(input())
q_ar=[]
for i in range(m):
    q_ar.append(int(input()))
for j in range(m):
    result=findfloor(ar_sorted,n,q_ar[j])
    if result == -1 or result==None:
        print(-2147483648)
    else:
        print(ar_sorted[result])
