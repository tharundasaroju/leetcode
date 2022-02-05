def findReplaceString(s: str, indices: list[int], sources: list[str], targets: list[str]) -> str:
    arr = [i+"" for i in s]
    print(arr)
    for i in range(len(indices)):
        if(s[indices[i]:indices[i]+len(sources[i])] == sources[i]):
            arr[indices[i]] = targets[i]
            for j in range(len(sources[i])):
                if(j!=0):
                    arr[indices[i]+j] = ""

    result = ""
    for word in arr:
        result += word

    print(result)



    print(s)


s = "vmokgggqzp"
i = [3,5,1]
sources = ["kg","ggq","mo"]
t = ["s","so","bfr"]

findReplaceString(s, i, sources, t)