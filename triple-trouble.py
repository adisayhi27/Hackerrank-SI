## using bit manipulation

def tripleTrouble(n,ar):
    ans = 0
    for i in range(30):
        c=0
        for j in range(n):
            if (checkBit(ar[j],i)==True):
                c+=1
        if (c%3!=0):
            ans+=1<<i
    print(ans)


def checkBit(n,k):
    new_num= n>>k
    return (new_num & 1)


m=int(input())
for i in range(m):
    n = int(input())
    ar = list(map(int,input().strip().split()))[:n]
    tripleTrouble(n,ar)
    
    
    
###########################################################################################

## Using Dictionary

def tripleTrouble1(n, arr):
    a = dict()
    for i in range(n):
        try:
            a[arr[i]] += 1  
        except KeyError:
            a[arr[i]] = 1
    
    for key, value in a.items():
        if value == 1:
            print(key)
m=int(input())
for i in range(m):
    n = int(input())
    ar = list(map(int,input().strip().split()))[:n]
    tripleTrouble1(n,ar)
