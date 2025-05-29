"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # insert copied nodes
        cur = head
        while cur:
            new_node = Node(cur.val)
            new_node.next = cur.next
            cur.next = new_node
            cur = new_node.next

        # set random node
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next # point to copied node
            cur = cur.next.next

        # separate two lists
        cur = head
        head_copy = Node(0)
        cur_copy = head_copy

        while cur:
            copy = cur.next
            cur_copy.next = copy
            cur_copy = copy

            cur.next = copy.next
            cur = cur.next
        
        return head_copy.next


# The following is recursion with Hash map version
# Recursive version risks stack overflow for large lists due to call stack usage
# Overall space: O(N) — from recursion stack and the hash map
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodesMapping = {}
        def copyList(root): 
            if not root:
                return None
            
            if root in nodesMapping:
                return nodesMapping[root]

            root2 = Node(root.val)
            nodesMapping[root] = root2
            
            root2.next = copyList(root.next)
            root2.random = copyList(root.random)
            
            return root2

        return copyList(head)
