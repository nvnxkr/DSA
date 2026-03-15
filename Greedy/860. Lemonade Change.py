# At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.
# Note that you do not have any change in hand at first.
# Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.

# Example 1:
# Input: bills = [5,5,5,10,20]
# Output: true
# Explanation: 
# From the first 3 customers, we collect three $5 bills in order.
# From the fourth customer, we collect a $10 bill and give back a $5.
# From the fifth customer, we give a $10 bill and a $5 bill.
# Since all customers got correct change, we output true.

from typing import List
def lemonadeChange(bills: List[int]) -> bool:
    n=len(bills)
    c5=0
    c10=0
    c20=0

    if bills[0]>5:
        return False
    for i in range(0,n):
        if bills[i]==5:
            c5+=1
        elif bills[i]==10:
            c10+=1
            c5-=1
        else:  # bills[i] == 20
            if c10 > 0 and c5 > 0:   # prefer 10+5
                c10 -= 1
                c5 -= 1
            elif c5 >= 3:            # otherwise use 3 fives
                c5 -= 3
            else:
                return False 

    if c5>=0 and c10>=0:
        return True
    else:
        return False
    
print(lemonadeChange([5,5,5,10,20]))
print(lemonadeChange([5,5,10]))
print(lemonadeChange([10,10]))

        