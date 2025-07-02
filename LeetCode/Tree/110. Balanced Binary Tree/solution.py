# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return 0, True

            left, leftBalanced = dfs(node.left)
            right, rightBalanced = dfs(node.right)

            curBalanced = abs(left - right) <= 1
            totBalanced = curBalanced and leftBalanced and rightBalanced

            return max(left, right) +1, totBalanced
        
        d, b = dfs(root)

        return b

# early-stop version
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def dfs(node):
            nonlocal balanced
            if not node or not balanced:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left - right) > 1:
                balanced = False

            return max(left, right) + 1

        dfs(root)
        return balanced
