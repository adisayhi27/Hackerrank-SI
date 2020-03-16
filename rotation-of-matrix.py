def rotmatrix(A,N):
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = A[i][j]
            A[i][j] = A[N - 1 - j][i]
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
            A[j][N - 1 - i] = temp

    for row in range(N):
        for col in range(N):
            print (A[row][col],end=' ')
        print()

m=int(input())
for i in range(m):
    n=int(input())
    mat = []
    for j in range(n):
        mat.append(list(map(int, input().split()))[:n])
    print("Test Case #" + str(i+1) + ":")
    rotmatrix(mat,n)
