# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop(-1)
            if node.val == p.val or node.val == q.val:
                return node
            elif p.val < node.val and q.val > node.val:
                return node
            elif q.val < node.val and p.val > node.val:
                return node
            
            if q.val < node.val:
                stack.append(node.left)
            else:
                stack.append(node.right)