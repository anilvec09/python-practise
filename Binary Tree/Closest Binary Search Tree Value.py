
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        items = []
        def traverse(node ):
            if not node:
                return
            nonlocal target
            if abs(target - node.val) == 0:
                items.append([node.val ,abs(target - node.val)])
            else:
                if target < node.val :
                    traverse(node.left)

                items.append([node.val ,abs(target - node.val)])

                if target > node.val:
                    traverse(node.right)


        traverse(root)
        print(items)
        items.sort(key=lambda x :x[1])
        return items[0][0]

