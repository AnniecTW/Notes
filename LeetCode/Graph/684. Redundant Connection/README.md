## 684. Redundant Connection
🔗 Link: [Redundant Connection](https://leetcode.com/problems/redundant-connection/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Graph<br>

<hr>

In this problem, a tree is an **undirected graph** that is connected and has no cycles.<br>

You are given a graph that started as a tree with `n` nodes labeled from `1` to `n`, with one additional edge added. The added edge has two **different** vertices chosen from `1` to `n`, and was not an edge that already existed. The graph is represented as an array `edges` of length n where `edges[i] = [ai, bi]` indicates that there is an edge between nodes `ai` and `bi` in the graph.<br>

Return an *edge* that can be removed so that the resulting graph is a tree of `n` nodes. If there are multiple answers, return the answer that occurs last in the input.



Example 1:<br>

<img src="https://github.com/user-attachments/assets/b3cd0d4d-ccbc-45cb-b678-d117f566cd9b" alt="tree with three nodes" width="200" />

>Input: edges = [[1,2],[1,3],[2,3]]<br>
Output: [2,3]<br>


Example 2:<br>
<img src="https://github.com/user-attachments/assets/473cd51a-a2d2-4535-a4e2-6db2ed1e07c7" alt="tree with five nodes" width="300"/>

>Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]<br>
Output: [1,4]<br>


Constraints:<br>

- n == edges.length
- 3 <= n <= 1000
- edges[i].length == 2
- 1 <= ai < bi <= edges.length
- ai != bi
- There are no repeated edges.
- The given graph is connected.

**Follow up**: Could you use search pruning to make your solution faster with a larger board?

<hr>

### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the length of `edges` be less than 3?<br>
2. Any constraints on time/space complexity?<br>
3. Can we assume the graph is always connected and contains exactly one cycle?<br>
4. Is it possible the input doesn't contain a redundant connection at all?<br>
5. Happy path - Input: edges = [[1,2],[1,3],[3,4],[2,4]]; Output: [2,4]
6. Edge case - Input: edges = [[1,2],[1,3],[2,3]]; Output: [2,3]

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. Graph
   - Pattern: Cycle detection in an undirected graph
   - Strategy: Union-Finde (Disjoint Set Union) with path compression
   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Use Union-Find data structure to track which nodes are in the same component. For each edge, if the two nodes are already connected, that means this edge would form a cycle — so it’s the redundant connection.<br>

1) Define UnionFind
   ```python
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
   ```
2) Initialize UnionFind with size n + 1 (since node numbering starts at 1)
3) For each edge (u, v) in edges:<br>
   If union(u, v) returns False, return `[u, v]` — this is the edge that forms a cycle
   ```python
   for u, v in edges:
       if not uf.union(u, v):
           return [u, v]

### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N is the nubmer of nodes

- Time Complexity: O(N * α(N)), where α(N) is the inverse Ackermann function (almost constant)<br>
  We process each edge once, and Union-Find operations are nearly constant time with path compression. <br>
- Space Complexity: O(N)<br>
  We maintain a `parent` array of size N+1 to track disjoint sets.<br>
