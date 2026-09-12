'''
In a warehouse, there is a row of barcodes, where the ith barcode is barcodes[i].

Rearrange the barcodes so that no two adjacent barcodes are equal. You may return any answer, and it is guaranteed an answer exists.

 

Example 1:

Input: barcodes = [1,1,1,2,2,2]
Output: [2,1,2,1,2,1]
Example 2:

Input: barcodes = [1,1,1,1,2,2,3,3]
Output: [1,3,1,3,1,2,1,2]
 
'''

from collections import Counter
from typing import List


class Solution:
    def rearrangeBarcodes(self, bar: List[int]) -> List[int]:
        cnt = Counter(bar)
        # cnt = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
        # ans=[]
        # while True:
        #     ch1,first=cnt[0]
        #     ch2,sec=cnt[1]
        #     if first!=0:
        #         ans.append(ch1)
        #     if sec !=0:
        #         ans.append(ch2)
        #     if first ==0 and sec==0:
        #         break
        #     cnt[0][0]-=1
        #     cnt[1][0]-=1
        #     cnt = sorted(cnt, key=lambda x: x[1], reverse=True)

        # return ans
        n = len(bar)
        ans = [0] * n
        cnt = Counter(bar)
        cnt = [list(x) for x in sorted(cnt.items(), key=lambda x: x[1], reverse=True)]
        i = 0

        for j in range(0, n, 2):
            ans[j] = cnt[i][0]
            cnt[i][1] -= 1
            if cnt[i][1] == 0:
                i += 1

        for k in range(1, n, 2):
            ans[k] = cnt[i][0]
            cnt[i][1] -= 1
            if cnt[i][1] == 0:
                i += 1
        return ans

