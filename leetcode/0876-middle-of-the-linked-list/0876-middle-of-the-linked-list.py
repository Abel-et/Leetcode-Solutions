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

        # go until prev node of the middle node
        while i < middle:
            dummy = dummy.next
            print(dummy.val)
            i+=1
        
        # if len is even return the second middle else return 
        return dummy if length%2 == 0 else dummy.next