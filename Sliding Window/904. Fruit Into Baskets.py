from typing import List

def totalFruit(fruits: List[int]) -> int:
    low=0
    high=0
    res=-1
    n=len(fruits)
    dic={}

    while high<n:

        dic[fruits[high]]=dic.get(fruits[high],0)+1

        if len(dic)>2:
            dic[fruits[low]]-=1
            if dic[fruits[low]]==0:
                del dic[fruits[low]]

            low+=1

        if len(dic)<=2:
            res=max(res,high-low+1)

        high+=1

    return res

print(totalFruit([1,2,3,2,2]))