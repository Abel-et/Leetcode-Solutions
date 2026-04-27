# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        container = deque([root])
        if root : 

            while container:
                # pop out the first element form the queue
                level = []
                for i in range(len(container)):
                    node = container.popleft()
                    level.append(node.val)

                    if node.left:
                        container.append(node.left)
                    if node.right:
                        container.append(node.right)
                result.append(level)
                
                
        return result
        
            





