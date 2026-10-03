# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            stack1 = []
            stack2 = []
            stack1.append(p)
            stack2.append(q)
            while stack1 and stack2:
                node1 = stack1.pop(-1)
                node2 = stack2.pop(-1)
                if node1 and node2:
                    if node1.val != node2.val:
                        return False
                    stack1.append(node1.left)
                    stack1.append(node1.right)
                    stack2.append(node2.left)
                    stack2.append(node2.right)
                elif node1 or node2:
                    return False
            return True
        
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop(-1)
            if node.val == subRoot.val:
                if isSameTree(node, subRoot):
                    return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False