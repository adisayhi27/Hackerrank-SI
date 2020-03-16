def largestPalindromic(n,s):
    max_len = 1
    low=0
    high=0
    for i in range(1,n):
        ## For odd characters in between required value ## E.g aba
        low = i-1
        high = i
        while low >= 0 and high < n and s[low] == s[high]:
            if high - low + 1 > max_len:
                max_len = high - low + 1
            low -= 1
            high += 1

        ## For even characters in between required value ## E.g abba
        low = i -1
        high = i + 1
        while low >= 0 and high < n and s[low] == s[high]:
            if high - low + 1 > max_len:
                max_len = high - low + 1
            low -= 1
            high += 1

    return max_len

m = int(input())
for i in range(m):
    n = int(input())
    s=input()[:n]
    print(largestPalindromic(n,s))
