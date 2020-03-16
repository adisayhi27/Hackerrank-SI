def wordVowCons(s,s_noSpace,word_len,s_len,VowelsCnt,ConsCnt):
    mydict = {}
    #vowelS = 'aeiou'
    for ch in s_noSpace:
        try:
            mydict[ch] += 1
        except KeyError:
            mydict[ch] = 1

    for k,v in mydict.items():
        if k == 'a':
            VowelsCnt += v
        elif k == 'e':
            VowelsCnt += v
        elif k == 'i':
            VowelsCnt += v
        elif k == 'o':
            VowelsCnt += v
        elif k == 'u':
            VowelsCnt += v

    ConsCnt = s_len - VowelsCnt

    print(str(word_len) + " " + str(VowelsCnt) + " " + str(ConsCnt))

if __name__ == "__main__":
    m=int(input())
    for i in range(m):
        s=input()#.split()
        word_len = len(s.split())
        s_noSpace=s.replace(" ","").lower()
        s_len = len(s_noSpace)
        VowelsCnt = 0
        ConsCnt = 0
        #s=''.join(s)
        wordVowCons(s,s_noSpace,word_len,s_len,VowelsCnt,ConsCnt)
        #print()
