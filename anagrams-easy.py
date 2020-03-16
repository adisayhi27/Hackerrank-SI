def stringAnagram(a,b):
    NoOfChars = 256
    count1 = [0]* NoOfChars
    count2 = [0]* NoOfChars

    if len(a) != len(b):
        return False

    for i in a:
        count1[ord(i)] += 1

    for j in b:
        count2[ord(j)] += 1

    for i in range(NoOfChars):
        if count1[i] != count2[i]:
            return False

    return True


m=int(input())
for i in range(m):
    a,b = input().split()
    print(stringAnagram(a,b))
