
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://leetcode.com/problems/binary-tree-inorder-traversal/
# RECURSION

def inorderTraversal(self, root: TreeNode) -> List[int]:
    if not root:
        return
    val = []
    def inorder(node):
        if node.left:
            inorder(node.left)
        val.append(node.val)
        if node.right:
            inorder(node.right)


    inorder(root)
    return val


# ITERATION
def inorderTraversal(self, root):
    stack = []

    res = []

    while True:

        if root:
            stack.append(root)
            root = root.left

        elif stack:
            root = stack.pop()
            res.append(root.val)
            root = root.right

        else:
            break

    return res