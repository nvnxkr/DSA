'''
Given an integer n, return the number of prime numbers that are strictly less than n.

 

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
 


'''

class Solution:
    def countPrimes(self, n: int) -> int:
        if n==0 or n==1:
            return 0
        if n==2:
            return 0

        prime=[1 for i in range(n)]
        prime[0]=0
        prime[1]=0
        cnt=0


        for i in range(2,int(n**0.5)+1):
            if prime[i]:
                for j in range(i*i,n,i):
                    prime[j]=0

        for n in prime:
            if n==1:
                cnt+=1
        
        return cnt




sol=Solution()
print(sol.countPrimes(10))