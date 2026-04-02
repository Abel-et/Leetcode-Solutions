# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        # the idea is just there is an array so ur task is to make the give arr in to bst
        #   to make binary search tree show follow binary search tempale which is mid = (left + right)//2
        #   this approach takes 
        #           first it takes the left element form root
                    # the find there mid and make it root
                    # after that 
        
        def game_changer(left , right):

            # base case which will replaced by mid that will increase when we are working on left part
            # decrease when we are working on the right part.
            if left > right :
                return None
            # find mid element on every func call
            mid = (left + right)//2

            # create a node then give left and right edge
            root = TreeNode(nums[mid])
            root.left = game_changer(left , mid - 1)
            root.right = game_changer(mid + 1 , right)
            return root
            
        return game_changer(0 , len(nums)-1)