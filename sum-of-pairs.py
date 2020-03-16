## Using 2 pointers

def sumOfPairs(ar,n):
    ar_sort=ar.sort()
    p1=0
    p2=n-1
    while(p1<p2):
        if (ar[p1]+ar[p2]==k):
            return True
        elif (ar[p1]+ar[p2]>k):
            p2-=1
        else:
            p1+=1
    return False


m=int(input())
for i in range(m):
    n,k=map(int,input().split())
    ar=list(map(int, input().split()))[:n]
    print(sumOfPairs(ar,n))

###############################################################

## Using binary Search

def sumOfPairsRecursive(ar,n,k):
    #ar=ar.sort()
    ar = sorted(ar)
    for i in range(n):
        a=ar[i]
        b=k-a
        if (BSR(ar,b,i+1,n-1)==True):
            return True
        #else:
         #   return False

def BSR(ar,b,lo,hi):
    mid = int((lo + hi) // 2)
    if (lo > hi):
        return False
    elif ar[mid]==b:
        return True
    elif b<ar[mid]:
        return BSR(ar,b,lo,mid-1)
    return BSR(ar,b,mid+1,hi)

if __name__ == "__main__":
    m=int(input())
    for i in range(m):
        n,k=map(int,input().split())
        ar=list(map(int, input().split()))[:n]
        #print(sumOfPairsRecursive(ar, n,k))
        res=sumOfPairsRecursive(ar, n, k)
        if res == None or res == 'False':
            print('False')
        else:
            print('True')
