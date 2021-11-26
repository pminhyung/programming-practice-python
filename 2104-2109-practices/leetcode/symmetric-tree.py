"""
BFS + queue

# False조건 : left가 없거나, right가 없거나 또는 둘다 있어도 다르거나
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSymmetric(self, root):
        if not root:
            return True

        q = deque([root.left, root.right])

        while q:
            t1, t2 = q.popleft(), q.popleft()

            if not t1 and not t2:
                continue
            elif (not t1 or not t2) or (t1.val != t2.val):
                return False

            q += [t1.left, t2.right, t1.right, t2.left]

        return True