def reverseBit(n,bitsize):
    binNo=bin(n)
    
    afterRev=binNo[-1:1:-1]
    afterRev=afterRev + (bitsize-len(afterRev)) * '0'
    
    print(int(afterRev,2))
    
    
m=int(input())
bitsize=32
for i in range(m):
    n=int(input())
    reverseBit(n,bitsize)
