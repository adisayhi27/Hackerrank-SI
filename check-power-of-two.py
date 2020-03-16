def poweroftwo(n):
    for i in range(n):
        j = int(input())
        count=0
        while(j>0):
            count += j & 1
            j >>= 1
        #return count
        if count == 1:
            print("True")
        else:
            print("False")
            
n = int(input())
poweroftwo(n)
