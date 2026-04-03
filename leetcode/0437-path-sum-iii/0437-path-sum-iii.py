# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cache  = {0:1}
        count = 0

        def dfs(root , current_sum):
            nonlocal count
            if not root : return

            current_sum += root.val
            old = current_sum - targetSum

            count += cache.get(old,0)
          
            cache[current_sum] = cache.get(current_sum , 0) + 1
           

            dfs(root.left, current_sum)
            dfs(root.right, current_sum)
            cache[current_sum] -= 1
        dfs(root,0)
        return count 