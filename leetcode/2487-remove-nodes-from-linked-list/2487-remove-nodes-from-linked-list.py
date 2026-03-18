# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Use a stack to maintain a monotonic decreasing sequence
        stack = []
        current = head
        
        while current:
            # While the current node is greater than the last node in the stack,
            # that last node must be removed (as it has a greater value to its right).
            while stack and current.val > stack[-1].val:
                stack.pop()
            
            stack.append(current)
            current = current.next
        
        # Step 2: Reconstruct the linked list from the nodes remaining in the stack
        if not stack:
            return None
            
        # Link the nodes in the stack together
        for i in range(len(stack) - 1):
            stack[i].next = stack[i + 1]
            
        # Ensure the last node points to None to avoid cycles
        stack[-1].next = None
        
        # The first element in the stack is the new head
        return stack[0]
