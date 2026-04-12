# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a, b = "", ""
        while l1:
            a += str(l1.val)
            l1 = l1.next
        while l2:
            b += str(l2.val)
            l2 = l2.next
        result = str((int(a[::-1]) + int(b[::-1])))
        
        result_digit = [int(i) for i in result[::-1]]

        dummy = ListNode(0)
        current = dummy 

        for digit in result_digit:
            current.next = ListNode(digit)
            current = current.next
        return dummy.next