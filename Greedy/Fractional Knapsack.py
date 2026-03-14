# Given two arrays, val[] and wt[] , representing the values and weights of items, and an integer capacity representing the maximum weight a knapsack can hold, determine the maximum total value that can be achieved by putting items in the knapsack. You are allowed to break items into fractions if necessary.
# Return the maximum value as a double, rounded to 6 decimal places.

# Examples :
# Input: val[] = [60, 100, 120], wt[] = [10, 20, 30], capacity = 50
# Output: 240.000000
# Explanation: By taking items of weight 10 and 20 kg and 2/3 fraction of 30 kg. Hence total price will be 60+100+(2/3)(120) = 240


def fractionalKnapsack(val, wt, capacity):
    #code here
    n=len(val)
    total=0
    pro=[]
    for i in range(n):
        temp=val[i]/wt[i]
        
        pro.append(temp)
    
    indices = sorted(range(n), key=lambda i: pro[i], reverse=True)
        
    for i in indices:
        if wt[i]<=capacity:
            total=val[i]+total
            capacity=capacity-wt[i]
        else:
            total=(capacity*pro[i])+total
            break
            
    return round(total,6)

print(fractionalKnapsack([60, 100, 120],[10, 20, 30],50))
print(fractionalKnapsack([10, 40, 30],[5, 4, 6],10))