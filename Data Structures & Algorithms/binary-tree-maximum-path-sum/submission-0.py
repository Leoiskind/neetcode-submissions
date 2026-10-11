# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.totals = []
        def summed(root):
            if root:
                left = summed(root.left)
                right = summed(root.right)
                self.totals.append(max(root.val, left + root.val, right + root.val, right + left + root.val))
                return(max(left + root.val, right + root.val, root.val))
            else:
                return 0
        summed(root)
        return max(self.totals)