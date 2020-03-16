import math

def cubeRoot(n,lo,hi):
    while(lo < hi):
        mid = (lo+hi)//2
        if mid * mid * mid == n :
            return mid
        elif mid * mid * mid < n :
            return cubeRoot(n,mid,hi)
        else:
            return cubeRoot(n,lo,mid)

def cubeRootNegative(n, lo, hi):
    while (lo < hi):
        mid = (lo + hi) // 2
        if mid * mid * mid == n:
            return mid
        elif mid * mid * mid < n:
            return cubeRootNegative(n, mid, hi)
        else:
            return cubeRootNegative(n, lo, mid)

if __name__ == "__main__":
    m=int(input())
    for i in range(m):
        n=int(input())
        # if n>0:
        #     lo = 0
        #     hi = n
        #     print(cubeRoot(n,lo,hi))
        # else:
        #     lo = n
        #     hi = 0
        #     print(cubeRootNegative(n, lo, hi))
        #     #print(-int(math.pow(abs(n), float(1) / 3))-1)
        if n==1:
            print("1")
        elif n==-1:
            print("-1")
        elif n>1:
            lo = 0
            hi = n
            print(cubeRoot(n,lo,hi))
        elif n <-1:
            lo = n
            hi = 0
            print(cubeRootNegative(n, lo, hi))
