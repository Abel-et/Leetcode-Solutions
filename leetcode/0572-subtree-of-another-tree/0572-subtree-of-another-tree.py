# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If the main tree is empty, subRoot can't be inside it
        if not root:
            return False
        
        # 1. If the current nodes match, check if the whole trees are identical
        if self.isSameTree(root, subRoot):
            return True
        
        # 2. Otherwise, look in the left child or the right child
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both are null, they are the same
        if not p and not q:
            return True
        # If one is null or values differ, they are NOT the same
        if not p or not q or p.val != q.val:
            return False
        
        # Check both left and right branches recursively
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
