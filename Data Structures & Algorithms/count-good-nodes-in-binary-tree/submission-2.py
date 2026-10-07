# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def checkNode(root, largest):
            if not root:
                return 0
            if root.val >= largest:
                largest = root.val
                return checkNode(root.left, largest) + 1 + checkNode(root.right, largest)
            else:
                return checkNode(root.left, largest) + checkNode(root.right, largest)
        
        largest = -float('inf')
        return checkNode(root, largest)