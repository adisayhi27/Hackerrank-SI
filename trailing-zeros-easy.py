def trailingZero(n):
    for i in range(n):
        k = int(input())
        j=5
        count=0
        while(k/j >= 1):
            count+=int(k/j)
            j*=5
        print(count)


n=int(input())
trailingZero(n)
