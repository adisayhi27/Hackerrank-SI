from operator import itemgetter
from collections import OrderedDict

def freqSort(lst,n):
    mydict={}
    cnt = 0
    for i in range(n):
        if lst[i] in mydict:
            mydict[lst[i]] += 1
        else:
            mydict[lst[i]] = 1

    sorted_x = OrderedDict(sorted(mydict.items(), key=itemgetter(1)))

    for elem in sorted_x:
        if sorted_x[elem] == 1:
            print(elem, end=" ")
        else:
            for i in range(sorted_x[elem]):
                print(elem, end=" ")

m=int(input())
for i in range(m):
    n=int(input())
    #lst=list(map(int, input().split()))[:n]
    arr = list(map(int, input().split()))[:n]
    lst = sorted(arr)
    freqSort(lst,n)
    print()
