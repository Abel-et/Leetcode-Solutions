# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        # the idea is like on our linked list session we do next next thing so 
        # in this problem also we use it left.left, right.right

        total = [0]
        

        def preOrder(root, total):
            if root is None:
                return 
            if root.val%2 == 0:
                if root.left is not None :
                    if root.left.left is not None:
                        total[0] += root.left.left.val
                    if root.left.right is not None:
                        total[0] += root.left.right.val
                if root.right is not None :
                    if root.right.right is not None:
                        total[0] += root.right.right.val
                    if root.right.left is not None:
                        total[0] += root.right.left.val
            preOrder(root.left, total)
            preOrder(root.right, total)
            
        preOrder(root, total)
        return total[0]
            