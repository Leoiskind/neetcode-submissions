# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightView = []
        stack = []
        curr = root
        highest = 0
        height = 0
        while curr:
            height += 1
            if height > highest:
                rightView.append(curr.val)
                highest = height
            if curr.left:
                stack.append(tuple([curr.left, height]))
            if not curr.right and stack:
                node = stack.pop(-1)
                height = node[1]
                curr = node[0]
            else:
                curr = curr.right
        return rightView