# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def inorderTraversal(self, root: TreeNode) -> List[int]:

        list = []
        self.recursive(root, list)
        return list

    def recursive(self, root, list):

        if root is None:
            return list

        if root.left:
            self.recursive(root.left, list)

        list.append(root.val)

        if root.right:
            self.recursive(root.right, list)
