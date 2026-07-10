'''
You are given two arrays: deadline[], and profit[], which represent a set of jobs, where each job is associated with a deadline, and a profit. Each job takes 1 unit of time to complete, and only one job can be scheduled at a time. You will earn the profit associated with a job only if it is completed by its deadline.

Your task is to find:

The maximum number of jobs that can be completed within their deadlines.
The total maximum profit earned by completing those jobs.
Examples :

Input: deadline[] = [4, 1, 1, 1], profit[] = [20, 10, 40, 30]
Output: [2, 60]
Explanation: Job1 and Job3 can be done with maximum profit of 60 (20+40).
Input: deadline[] = [2, 1, 2, 1, 1], profit[] = [100, 19, 27, 25, 15]
Output: [2, 127]
Explanation: Job1 and Job3 can be done with maximum profit of 127 (100+27).
Input: deadline[] = [3, 1, 2, 2], profit[] = [50, 10, 20, 30]
Output: [3, 100]
Explanation: Job1, Job3 and Job4 can be completed with a maximum profit of 100 (50 + 20 + 30).
'''

class DisJointSet:
    def __init__(self,V):
        self.parent=[i for i in range(V+1)]
        self.rank=[0]*(V+1)
    
    def find(self,x):
        if x==self.parent[x]:
            return x
        
        self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
class Solution:
    def jobSequencing(self, deadline, profit):
        # code here
        chart=[0]*max(deadline)
        k=0
        dsu=DisJointSet(len(chart))
        
        n=len(profit)
        pd=[[profit[i],deadline[i]] for i in range(n)]
        pd.sort(reverse=True)
        
        total=cnt=0
        
        for p,d in pd:
            slot=dsu.find(d)
            if slot>0:
                cnt+=1
                total+=p
                dsu.parent[slot] = dsu.find(slot - 1)
        return [cnt,total]
        
        
sol=Solution()
print(sol.jobSequencing([4, 1, 1, 1], [20, 10, 40, 30]))