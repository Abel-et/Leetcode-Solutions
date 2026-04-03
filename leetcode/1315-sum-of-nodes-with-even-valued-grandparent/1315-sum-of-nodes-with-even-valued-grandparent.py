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

        self.total = 0

        def dfs(node, parent , grandparent):
            
            # base case is the cild (node)is not null
            if not node:
                return 
            # if grand parent is not none and it val is eve 
            if grandparent and grandparent.val%2 == 0:
                self.total += node.val

            dfs(node.left , node, parent )
            dfs(node.right, node, parent)
        dfs(root, None , None)
        return self.total