## 2013. Detect Squares
🔗 Link: [Detect Squares](https://leetcode.com/problems/detect-squares/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Hash<br>

<hr>
You are given a stream of points on the X-Y plane. Design an algorithm that:<br>

- **Adds** new points from the stream into a data structure. **Duplicate** points are allowed and should be treated as different points.
- Given a query point, **counts** the number of ways to choose three points from the data structure such that the three points and the query point form an **axis-aligned** square with **positive area.**

Implement the `DetectSquares` class:<br> 
- `DetectSquares()` Initializes the object with an empty data structure.
- `void add(int[] point)` Adds a new point `point = [x, y]` to the data structure.
- `int count(int[] point)` Counts the number of ways to form axis-aligned squares with point `point = [x, y]` as described above.

  
Example 1:<br>
![image-3](https://github.com/user-attachments/assets/cc9803b5-e731-420b-b871-96dd51694485)

Input<br>
>["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]<br>
>[[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]<br>
<br>

Output<br>
>[null, null, null, null, 1, 0, null, 2]<br>
<br>

Explanation<br>
>DetectSquares detectSquares = new DetectSquares();<br>
>detectSquares.add([3, 10]);<br>
>detectSquares.add([11, 2]);<br>
>detectSquares.add([3, 2]);<br>
>detectSquares.count([11, 10]); // return 1. You can choose: The first, second, and third points<br>
>detectSquares.count([14, 8]);  // return 0. The query point cannot form a square with any points in the data structure.<br>
>detectSquares.add([11, 2]);    // Adding duplicate points is allowed.<br>
>detectSquares.count([11, 10]);<br>
>// return 2. You can choose:<br>
>//   - The first, second, and third points<br>
>//   - The first, third, and fourth points<br>


Constraints:<br>

- point.length == 2
- 0 <= x, y <= 1000
- At most 3000 calls in total will be made to `add` and `count`.
<hr>

### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Any requirements on time/space complexity?<br>
2. Can the same point be added multiple times? (Double check edge case ) <br>
2. Happy path -<br>
   Input:<br>
   ```python
   DetectSquares detectSquares = new DetectSquares();
   detectSquares.add([0, 0]);
   detectSquares.add([2, 2]);
   detectSquares.add([0, 2]);
   detectSquares.count([2, 0]);
   # These four points form a square with a side length of 2
   ```
   Output: `1`<br>

4. Edge case -<br>
   Input:<br>
   ```python
   DetectSquares detectSquares = new DetectSquares();
   detectSquares.add([0, 0]);
   detectSquares.add([0, 0]);
   detectSquares.add([0, 0]);
   detectSquares.count([0, 0]);
   ```
   Output: `0`<br>

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. 2D geometry / Hash map frequency counting
   - Use square property to find valid squares: fix the given point, then find another point with the same x-coordinate to determine the potential side length, then infer the other two points based on that.
   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: We use a nested `defaultdict` to record the frequency of each point. To count how many squares exist with a queried point as one corner, enumerate all known y1 with the same x, and the coordinates of the possible opposite corners can then be calculated. Finally multiply frequencies of the 3 relevant points and sum up.<br>

1) `from collections import defaultdict`
2) Create a nested defaultdict to count each point's frequency
   ```python
   class DetectSquares:

    def __init__(self): self.pointCount = defaultdict(lambda: defaultdict(int))
   ```
3) Increment the frequency of a given point by 1 in each `add` operation 
   ```python
   def add(self, point: List[int]) -> None:
        self.pointCount[point[0]][point[1]] += 1
   ```
   
4) In `count` operation, first initailize the result `res = 0`, then get the coordinate of `point` through (x, y)
   ```python
   def count(self, point: List[int]) -> int:
        res = 0
        x, y = point
   ```
5) Iterate points `y1` having the same X-coordinate with `point`: `for y1 in self.pointCount[x]:`
   - Calculate `d = y - y1` as side length of a square: `d = y - y1`
   - If `d` is 0, indicating the points overlap, skip this loop :
     ```python
     if d == 0:
                continue
     ```
   - Calculate the X-coordinates of the rest two points of the square: `x1, x2 = x + d, x - d`
   - Count the number of valid squares by multiplying the frequency of the other three points and then sum up these count
     ```python
     res += self.pointCount[x1][y] * self.pointCount[x1][y1] * self.pointCount[x][y1]
     res += self.pointCount[x2][y] * self.pointCount[x2][y1] * self.pointCount[x][y1]
     ```
6) return `res`
    
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution


Assume N is the number of **unique** y-values for a given `x`

- Time Complexity: `add`: O(1) and `count`: O(N)<br>
  For `count` operation, all points share the same x-coordinate in the worst case, the runtime would be O(N) due to the iteration step.<br>
- Space Complexity: O(K)<br>
  In worst case, N unique points → each stored separately in nested defaultdict.<br>
