# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # arr = []

        # this is the first way 

        # def Travers(node):
        #     if node is None:
        #         return []
        #     arr.append(node.val)
        #     Travers(node.left)
        #     Travers(node.right)
        # Travers(root)
            
        # return arr
        
        # for the secode way
        if root is None:
            return []
        return [root.val] +  self.preorderTraversal(root.left) +  self.preorderTraversal(root.right)