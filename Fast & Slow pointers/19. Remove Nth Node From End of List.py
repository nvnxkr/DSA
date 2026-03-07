# Given the head of a linked list, remove the nth node from the end of the list and return its head.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(head, n):
        count = 0
        temp = head
        while temp:
            temp = temp.next
            count += 1

        if count == n:
            return head.next

        count = count - n - 1

        temp = head

        while count != 0:
            count -= 1
            temp = temp.next

        temp.next = temp.next.next

        return head
