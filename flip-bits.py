# Function that count set bits 
def FlippedCount(n): 
    for i in range(n):
        a,b = map(int,input().split())
        c = a^b
        count = 0
        while c: 
            count += c & 1
            c >>= 1
        print(count)
    
# Driver code 
n = int(input())
FlippedCount(n)
