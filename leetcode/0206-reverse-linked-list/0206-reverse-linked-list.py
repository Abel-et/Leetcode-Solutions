# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # arr hold the give elemntes linked list
        result = []
        if head is None:
            return None
        
        temp = head
        # adding all linked list elemnets into arr
        while temp:
            result.append(temp.val)
            temp = temp.next

        # reversig the give arr elements 
        result.reverse()
       
    #   changing the arr elemnets into linked list
        dummy = ListNode()
        current = dummy

        for element in result:
            current.next = ListNode(element)
            current = current.next
        return dummy.next