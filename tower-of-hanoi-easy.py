def towerOfHanoi(n,fr,to,aux):
    if n==1:
        print("Move 1"+" from "+str(fr)+" to "+str(to))
        return
    towerOfHanoi(n-1,fr,aux,to)    
    print("Move "+str(n)+" from "+str(fr)+" to "+str(to))
    towerOfHanoi(n-1,aux,to,fr)
    

m=int(input())
for i in range(m):
    n=int(input())
    print(pow(2,n)-1)
    towerOfHanoi(n,"A", "C", "B")
