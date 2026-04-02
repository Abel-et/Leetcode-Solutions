# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # we want to know if the given  tree is symmetrical equal so 
        # check the left part and the right part are equal at leaft point opositily 

        def dfs(LEFT, RIGHT):
            # if both are none is cool no error 
            if not LEFT and not RIGHT:
                return True

            # if one of them is not none there is a difference so return false
            if not LEFT or not RIGHT:
                return False
            
            # other wise check recursively  the value of right and left and the most left and the most right are equal .
            return LEFT.val == RIGHT.val and dfs(LEFT.left , RIGHT.right) and dfs(LEFT.right, RIGHT.left)
        return dfs(root.left, root.right)