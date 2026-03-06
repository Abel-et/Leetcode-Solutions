# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        rabbit , tirot = head, head
        cycle = False

        # phase one checking if there is a cycle
        while rabbit is not None and rabbit.next is not None:
            tirot = tirot.next
            rabbit = rabbit.next.next
            if rabbit== tirot:
                cycle = True
                break
           
        
        # phase to finding the starting node
        if cycle:
            start = head
            while start != rabbit:
                start =start.next
                rabbit = rabbit.next
            return start
        else:
            return None