from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def is_symmetric(self, root: TreeNode) -> bool:
        return self.is_mirror(root, root)

    def is_mirror(self, t1, t2):

        # 두 개의 루트가 None 이면 True
        if not t1 and not t2:
            return True

        # 두 루트 중 하나가 None 이면 False
        if not t1 or not t2:
            return False

        return t1.val == t2.val and self.is_mirror(t1.right, t2.left) and self.is_mirror(t1.left, t2.right)
