# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node):
            if not node:
                return True, float('inf'), float('-inf'), 0
            
            l_bst,n_min, n_max, n_sum = dfs(node.left)
            r_bst,nr_min, nr_max, nr_sum = dfs(node.right)

            if l_bst and r_bst and n_max < node.val < nr_min:
                curr = n_sum + nr_sum + node.val
                self.ans = max(curr, self.ans)
                return True ,min(n_min, node.val), max(nr_max, node.val), curr
            return False , float('-inf'), float('inf'), 0 

        dfs(root)
        return self.ans
