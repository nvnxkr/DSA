def groupAnagrams( strs):
    dic={}

    for st in strs:
        count=[0]*26

        for ch in st:
            count[ord(ch)-ord('a')]+=1

        if tuple(count) not in dic:  #tuple is used because it is immutable 
            dic[tuple(count)]=[]

        dic[tuple(count)].append(st)

    return list(dic.values())

strs = ["eat","tea","tan","ate","nat","bat"]

print(groupAnagrams(strs))