# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # create dummy node
        dummy = ListNode()
        dummy.next = head

        # find the lenght of the list 
        length = 0
        temp = dummy
        while temp:
            length +=1
            temp = temp.next

        # finding the middle node
        middle = length//2
        i = 0
        while i < middle-1:
            dummy = dummy.next
            i+=1
        
        return dummy.next if length%2 == 0 else dummy.next.next