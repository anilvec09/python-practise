# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if not root:
            return

        tilt = []
        if not root.left and not root.right:
            return
        if root.left and root.right:
            tilt.append(abs(root.left.val - root.right.val))
        if root.left and not root.right:
            tilt.append(root.left.val)
        if root.right and not root.left:
            tilt.append(root.right.val)
        self.findTilt(root.left)
        self.findTilt(root.right)
        return sum(tilt)
