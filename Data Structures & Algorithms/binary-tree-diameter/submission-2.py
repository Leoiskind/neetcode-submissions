# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(root):
            if not root:
                return 0
            return 1 + max(height(root.left), height(root.right))

        def count(root):
            return height(root.left) + height(root.right)
        maxD = 0
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop(-1)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            diam = count(node)
            if diam > maxD:
                maxD = diam
        
        return maxD
            