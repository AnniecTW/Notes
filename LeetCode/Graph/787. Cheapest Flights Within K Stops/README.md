## 787. Cheapest Flights Within K Stops
🔗 Link: [Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Graph<br>

<hr>

There are `n` cities connected by some number of `flights`. You are given an array `flights where flights[i] = [fromi, toi, pricei]` indicates that there is a flight from city `fromi` to city `toi` with cost `pricei`.<br>

You are also given three integers `src`, `dst`, and `k`, return the cheapest price from `src` to `dst` with at most `k` stops. If there is no such route, return `-1`.<br>



Example 1:<br>


<img src="https://github.com/user-attachments/assets/e3c5e7cc-e1c8-41ae-8ddb-1211dd1d1d87" alt="graph with 4 nodes" width="200" />

>Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1<br>
Output: 700<br>
Explanation:<br>
The graph is shown above.<br>
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.<br>
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.<br>


Example 2:<br>

<img src="https://github.com/user-attachments/assets/e38a3e5d-fa19-4f2c-b1a3-5126597ba5ed" alt="graph with 3 nodes" width="300"/>

>Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1<br>
Output: 200<br>
Explanation:<br>
The graph is shown above.<br>
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.<br>

Example 3:<br>

<img src="https://github.com/user-attachments/assets/5cedf941-acd2-42bc-a798-c07ed13f986d" alt="graph with 3 nodes" width="300"/>

>Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0<br>
Output: 500<br>
Explanation:<br>
The graph is shown above.<br>
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.<br>


Constraints:<br>

- 1 <= n <= 100
- 0 <= flights.length <= (n * (n - 1) / 2)
- flights[i].length == 3
- 0 <= fromi, toi < n
- fromi != toi
- 1 <= pricei <= 104
- There will not be any multiple flights between two cities.
- 0 <= src, dst, k < n
- src != dst

<hr>

### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Any constraints on time/space complexity?<br>
2. Can `flights` be empty or contains empty rows? <br>
3. Happy path - Input: flights = [[0,1,100],[1,2,100],[0,2,50]], src = 0, dst = 2, k = 1; Output: 50
6. Edge case - Input: flights = [[]], src = 0, dst = 2, k = 0; Output: -1
   
### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. BFS / Queue
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
