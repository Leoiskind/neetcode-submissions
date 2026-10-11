# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.pos = 0
        ids = {}
        for i, j in enumerate(inorder):
            ids[j] = i
        l = 0
        r = len(inorder) - 1
        def build(left, right):
            if left<=right:
                node = TreeNode(preorder[self.pos])
                self.pos += 1
                mid = ids[node.val]
                node.left = build(left, mid-1)
                node.right = build(mid+1, right)
                return node
            else:
                return None
        
        return build(l, r)

