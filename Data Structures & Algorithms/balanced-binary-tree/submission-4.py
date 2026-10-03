# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if not node:
                return 0, True
            left, lT = check(node.left)
            right, rT = check(node.right)
            balanced = lT and rT and abs(left - right) <= 1
            return 1 + max(left, right), balanced
        return check(root)[1]
