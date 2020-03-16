def rght(n):
    if (n==1):
        return print('*')
    for i in range(1,n+1,1):
        print((n-i) * ' ', end='')
        print(i * '*')

m=int(input())
for i in range(m):
    n=int(input())
    print("Case #"+str(i+1)+':')
    rght(n)
