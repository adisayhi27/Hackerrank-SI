import math

def hollowdiamond(n):
    j=1
    for i in range((math.ceil(n/2))+1,1,-1):
        if i == (math.ceil(n/2)+1):
            print((i - 2) * ' ' + str('*'))
        else:
            print((i-2)* ' ' +str('*') + j * ' ' + str('*'))
            j+=2

    for j in range(1,math.ceil(n/2),1):
        if (j==1):
            k = ((math.floor(n/2)*2) - ((2*j)+1))
            if k==-1:
                print(j * ' ' + str('*'))
            else:
                print(j * ' ' + str('*') + k * ' ' + str('*'))
            k-=2
        elif (j == math.ceil(n/2)-1):
            print(j* ' ' +str('*'))
        else:
            print(j * ' ' + str('*') +  k* ' '  + str('*'))
            k-=2



m=int(input())
for i in range(m):
    n=int(input())
    print("Case #"+str(i+1)+':')
    hollowdiamond(n)
