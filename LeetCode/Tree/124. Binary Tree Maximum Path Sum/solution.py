# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')

        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            cur_max = max(left, 0) + max(right, 0) + node.val  # Maximum path sum through the current node (can take both left and right)
            ans = max(ans, cur_max)

            return max(left, right, 0) + node.val  # Maximum path sum to return to parent (can only take one side)

        dfs(root)
        return ans
