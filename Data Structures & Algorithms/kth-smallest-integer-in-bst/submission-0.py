# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []

        def push_left(node):
            while node:
                stack.append(node)
                node = node.left
        
        push_left(root)
        for i in range(k):
            node = stack.pop(-1)
            if i == k-1:
                return node.val
            push_left(node.right)

        