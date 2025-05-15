# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mapping = {val: i for i, val in enumerate(inorder)}

        preOrder = deque(preorder)

        def build(start, end):
            if start > end:
                return None
            node = TreeNode(preOrder.popleft())
            mid = mapping[node.val]

            node.left = build(start, mid - 1)
            node.right = build(mid + 1, end)

            return node
        
        return build(0, len(preorder) - 1)
