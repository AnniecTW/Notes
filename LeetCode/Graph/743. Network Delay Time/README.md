## 743. Network Delay Time
🔗 Link: [Network Delay Time](https://leetcode.com/problems/network-delay-time/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Graph<br>

<hr>

You are given a network of `n` nodes, labeled from `1` to `n`. You are also given `times`, a list of travel times as directed edges `times[i] = (ui, vi, wi)`, where `ui` is the source node, `vi` is the target node, and `wi` is the time it takes for a signal to travel from source to target.<br>

We will send a signal from a given node k. Return the minimum time it takes for all the `n` nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return `-1`.<br>


Example 1:<br>


<img src="https://github.com/user-attachments/assets/f7d7e43f-c7e8-4300-be1d-7372d21ab4a5" alt="DAG" width="150" />

>Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2<br>
Output: 2<br>

Example 2:<br>

>Input: times = [[1,2,1]], n = 2, k = 1<br>
Output: 1<br>

Example 3:<br>

>Input: times = [[1,2,1]], n = 2, k = 2<br>
Output: -1<br>


Constraints:<br>

- 1 <= k <= n <= 100
- 1 <= times.length <= 6000
- times[i].length == 3
- 1 <= ui, vi <= n
- ui != vi
- 0 <= wi <= 100
- All the pairs `(ui, vi)` are unique. (i.e., no multiple edges.)

**Follow up**: Could you use search pruning to make your solution faster with a larger board?

<hr>

### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Are there self edges in the problem?<br>
2. Can the graph be disconnected? <br>
3. Are all edge weights positive? <br>
4. Any constraints on time/space complexity?<br>
5. Happy path - Input: edges = [[1,2,4]], n = 2, k = 1; Output: 4
6. Edge case - Input: edges = [[1,2,4]], n = 3, k = 3; Output: -1

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. Graph / Dijkstra
   - Pattern: The min time it takes for all the nodes to receive the signal from a given node equals to the max shortest time among the time edges
   - Strategy: Use Dijkstra's algorithm to compute the shortest path from the starting node to all other nodes, and take the max of these values. Since all edge weights are positive, Dijkstra is appropriate here.
   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Use Dijkstra to find the shortest path, then get the max values among the paths which equals to the minimum time it takes for all the nodes to receive the signal.<br>

1) Import required library
   ```python
   from collections import defaultdict
   import heapq
   ```
2) Initialize `heap` with node `k` and `dist` array with size n + 1 (since node numbering starts at 1)
3) Set `dist[k] = 0`
4) Build adjacency list<br>
   ```python
   adjacency = defaultdict(list)
   for src, dst, time in times:
       adjacency[src].append((dst, time))
5) Use Dijkstra algorithm with heap to calculate the shortest path
   ```python
   while heap:
       shortest, node = heapq.heappop(heap)
       if shortest > dist[node]:
           continue
            
       for dst, time in adjacency[node]:

           if shortest + time < dist[dst]:
               dist[dst] = shortest + time

               heapq.heappush(heap, (dist[dst], dst))
6) Get the max value in `dist[1:]` and return it. If it's a non-integer value, return `-1`
   ``` python
   res = max(dist[1:]) # since nodes are 1-indexed
   return -1 if res == float('inf') else res

   
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N is the nubmer of nodes and E is the number of edges

- Time Complexity: O(E log N)<br>
  Each edge can trigger at most one heap.push() operation. Since each heap operation takes O(log N) time and there are E edges, the total time complexity is O(E log N). <br>
- Space Complexity: O(N + E)<br>
  1. `dist` dictionary stores shortest distances for N nodes → O(N)<br>
  2. `adjacency` list stores all edges → O(E)<br>
  3. `heap` can contain up to N nodes in the worst case → O(N)
