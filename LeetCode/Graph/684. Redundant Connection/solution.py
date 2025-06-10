class Unionfind:
    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        RootU = self.find(u)
        RootV = self.find(v)

        if RootU == RootV:
            return False
        
        self.parent[RootU] = RootV
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = Unionfind(n + 1)

        for u, v in edges:
            if not uf.union(u, v):
                return [u, v]
