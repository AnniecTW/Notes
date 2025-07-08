## 621. Task Scheduler
🔗 Link: [Task Scheduler](https://leetcode.com/problems/task-scheduler/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Array / Greedy<br>

<hr>

You are given an array of CPU `tasks`, each labeled with a letter from A to Z, and a number `n`. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least `n` intervals between two tasks with the same label.

Return the **minimum** number of CPU intervals required to complete all tasks.

Example 1:<br>

>Input: tasks = ["A","A","A","B","B","B"], n = 2<br>
Output: 8<br>
Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.<br>
After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

Example 2:<br>

>Input: tasks = ["A","C","A","B","D","B"], n = 1<br>
Output: 6<br>
Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.<br>
With a cooling interval of 1, you can repeat a task after just one other task.

Example 3:<br>

>Input: tasks = ["A","A","A", "B","B","B"], n = 3<br>
Output: 10<br>
Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.<br>
There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.


Constraints:<br>

- 1 <= tasks.length <= 10<sup>4</sup>
- tasks[i] is an uppercase English letter.
- 0 <= n <= 100


<hr>

### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can `tasks` be empty?<br>
2. Any constraints on time/space complexity?<br>
3. Happy path - tasks = ["A","A","A","B","C","D"], n = 2; Output: 7;<br> Explanation: A valid sequence is: A -> B -> C -> A -> D -> idle -> A

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. Greedy
   - Place the most frequent task first, with at least `n` intervals between the same task. Fill the rest with other tasks or idle time. (Greedy placement strategy)
   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Schedule the most frequent task with `n` intervals between them, then greedily fill remaining slots with other tasks or idles as needed. 

1) Count each task: `counter = Counter(tasks)`
2) Find the maximum frequency: `maxFreq = max(counter.values())`
3) Count how many tasks have this maximum frequency:
   ```python
   max_count = sum(1 for freq in counter.values() if freq == maxFreq)
   ```
4) Compute the minimum required intervals:
   ```python
   min_len = (maxFreq - 1) * (n + 1) + max_count
   ```
   - `(maxFreq - 1)` is the number of full gaps between the most frequent tasks
   - `(n + 1)` accounts for each group: `n` idle slots + 1 task
   - `max_count` is the number of tasks with the maximum frequency, occupying the final group
5) Return `max(min_len, len(tasks))`
   - In some cases, there are enough tasks to fully occupy all slots without idle time
   
    
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N represents the length of tasks

- Time Complexity: O(N)<br>
  `Counter(tasks)` takes O(N), and we iterate through `counter.values()` twice. Total time: O(N) <br>
- Space Complexity: O(1)<br>
  Although `Counter(tasks)` stores frequency counts, there are at most 26 possible task types (A–Z), so the space used is constant.
