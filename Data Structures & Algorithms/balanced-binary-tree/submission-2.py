# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def findHeight(node):
            if node.left and node.right:
                return max(findHeight(node.left), findHeight(node.right)) + 1
            elif node.left:
                return findHeight(node.left) + 1
            elif node.right:
                return findHeight(node.right) + 1
            else:
                return 1
        def balanced(root):
            if not root:
                return True

            if root.left and root.right:
                diff = findHeight(root.left) - findHeight(root.right)
                if diff <= 1 and diff >= -1:
                    print(diff)
                    return True
                else:
                    return False
            elif root.left:
                if findHeight(root.left) <= 1:
                    return True
                return False
            elif root.right:
                if findHeight(root.right) <= 1:
                    return True
                return False
            else:
                return True
        stack = []
        if root:
            stack.append(root)
        while stack:
            node = stack.pop(-1)
            if not balanced(node):
                return False
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return True