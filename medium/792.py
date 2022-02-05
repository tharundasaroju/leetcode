def numMatchingSubseq(s: str, words: list[str]) -> int:
    while(len(s)>0 and sum(len(word) for word in words)):
        letter = s[0]
        s = s[1:]
        for i in range(len(words)):
            if(len(words[i])>0 and words[i][0]==letter):
                print("yes", letter, words[i])
                words[i] = words[i][1:]
    
    print(words)

