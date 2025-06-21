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

<img src="https://github.com/user-attachments/assets/e38a3e5d-fa19-4f2c-b1a3-5126597ba5ed" alt="graph with 3 nodes" width="200"/>

>Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1<br>
Output: 200<br>
Explanation:<br>
The graph is shown above.<br>
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.<br>

Example 3:<br>

<img src="https://github.com/user-attachments/assets/5cedf941-acd2-42bc-a798-c07ed13f986d" alt="graph with 3 nodes" width="200"/>

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
6. Edge case - Input: flights = [], src = 0, dst = 2, k = 0; Output: -1
   
### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. BFS + Queue
   - Pattern: The problem requires cheapest price from `src` to `dst` within `k` stops. Generally, Dijkastra's algorithm can only calculate cheapest price with all possible number of stops.
   - Strategy: Nonetheless, We can simply use a queue to perform BFS. During the process, we limit the number of possible stops to get the cheapest price from `src` to `dst` within `k` stops.
   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Use queue to record `(accumulated price, stops, node)` for BFS. During the process, update the cheapest price from `src` to `dst` when encounter smaller value, and break the loop once reach the limit of `stops`. <br>

1) Initilize `cost` array to record the lowest cost from `src` to `dst` within `k` stops
   ```python
   cost = [float('inf') for _ in range(n)]
   cost[src] = 0
   ```
2) Initialize `graph` as an adjacency list to record the relation between nodes
   ```python
   from collections import defaultdict, deque
   graph = defaultdict(list)
   for s, d, p in flights:
       graph[s].append((d, p))
   ```
3) Perform BFS and update cheapest price if smaller value is met, and break the loop once `stops` reaches the limit<br>
   ```python
   queue = deque([(0, src, 0)]) # price, node, stops
   while queue:
       price, node, stops = queue.popleft()

       if stops > k:
            break

       for d, p in graph[node]:
           if cost[d] > p + price:
               cost[d] = p + price
               queue.append((p + price, d, stops + 1))
 4) If `cost[dst]` hasn't been updated to a number, return `-1`; otherwise, return `cost[dst]`

### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N is the nubmer of nodes, E is the length of `flights`, and K is the limitation of stops

- Time Complexity: O(E + K * N)<br>
  O(E) to build the adjacency list. In the worst case, each node is visited up to K times in the BFS queue.<br>
- Space Complexity: O(E + K * N)<br>
  O(E) for the graph. O(N) for the cost array. O(K * N) for the BFS queue.<br>

This approach works efficiently under the assumption of non-negative edge weights and small `k`.<br>
If negative costs exist, we’d need to switch to Bellman-Ford.
