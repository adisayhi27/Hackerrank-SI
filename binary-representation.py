def BinaryRep(n):
    if (n>1):
        BinaryRep(n//2)
    print(n%2, end="")
        
n = int(input())
for i in range(n):
    j = int(input())
    BinaryRep(j)
    print()
