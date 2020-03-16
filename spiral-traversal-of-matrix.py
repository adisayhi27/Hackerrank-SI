def diagonalmat(mat,n):
    a=0 #Starting row index
    b=0 #Starting column index
    c=n #Ending column index
    d=n #Ending row index
    while(a<c and b<d):
        for i in range(b,c):
            print(mat[a][i], end=" ")
        a+=1

        for i in range(a,d):
            print(mat[i][c-1], end=" ")
        c-=1

        if (a<d):
            for i in range(c-1,(b-1),-1):
                print(mat[d-1][i], end=" ")
            d-=1

        if (b<c):
            for i in range(d-1,(a-1),-1):
                print(mat[i][b], end=" ")
            b+=1


m=int(input())
for i in range(m):
    n=int(input())
    mat = []
    for j in range(n):
        mat.append(list(map(int, input().split()))[:n])
    #print(mat)
    #print("Test Case #" + str(i+1) + ":")
    diagonalmat(mat,n)
    print()
