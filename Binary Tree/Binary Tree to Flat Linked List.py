#
# Given a binary tree, flatten it to a linked list in-place.
#
# For example, given the following tree:
# 1
#    / \
#   2   5
#  / \   \
# 3   4   6
# The flattened tree should look like
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def flat(root):
            if not root:
                return
            flat(root.right)
            flat(root.left)
            root.right = self.prev
            root.left = None
            self.prev = root
        self.prev = None
        flat(root)