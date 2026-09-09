'''
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
Example 2:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]
Example 3:

Input: l1 = [0], l2 = [0]
Output: [0]
'''

# Definition for singly-linked list.
from pyparsing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        def reverse(node):
            prev = None
            curr = node
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        def add(l1, l2):
            summ = 0
            carry = 0
            res = ListNode()
            curr = res
            while l1 or l2:
                summ = carry
                if l1:
                    summ += l1.val
                    l1 = l1.next
                if l2:
                    summ += l2.val
                    l2 = l2.next

                carry = summ // 10
                total = summ % 10

                curr.next = ListNode(total)
                curr = curr.next
            if carry:
                curr.next = ListNode(carry)
            return res.next

        fir = reverse(l1)
        sec = reverse(l2)

        final = add(fir, sec)

        return reverse(final)
