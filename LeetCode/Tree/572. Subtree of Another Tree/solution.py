# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursion: O(N * M)
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSame(r, s):
            if not r and not s:
                return True
            if not r or not s:
                return False
            if r.val != s.val:
                return False
            return isSame(r.left, s.left) and isSame(r.right, s.right)
        
        if not root:
            return False
        if isSame(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


# Serialization: O(N + M)
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialize(node):
            if not node:
                return '|#|'
            return f"|{node.val}|" + serialize(node.left) + serialize(node.right)
        
        return serialize(subRoot) in serialize(root)
