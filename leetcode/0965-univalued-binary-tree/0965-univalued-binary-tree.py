# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        start = root.val
        container = deque([root])

        while container:
            node = container.popleft()

            if node.val != start:
                return False

            if node.left:
                container.append(node.left)
                
            if node.right:
                container.append(node.right)
        return True

