## 146. LRU Cache
🔗 Link: [LRU Cache](https://leetcode.com/problems/lru-cache/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Hash<br>

<hr>
Design a data structure that follows the constraints of a [Least Recently Used (LRU) cache](https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU).<br>

Implement the `LRUCache` class:<br>
- `LRUCache(int capacity)` Initialize the LRU cache with positive size `capacity`.
- `int get(int key)` Return the value of the `key` if the key exists, otherwise return `-1`.
- `void put(int key, int value)` Update the value of the `key` if the `key` exists. Otherwise, add the `key-value` pair to the cache. If the number of keys exceeds the `capacity` from this operation, evict the least recently used key.

The functions `get` and `put` must each run in `O(1)` average time complexity.<br>

Example 1:<br>

> Input<br>
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]<br>
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]<br>
Output<br>
[null, null, null, 1, null, -1, null, -1, 3, 4]<br>

> Explanation<br>
LRUCache lRUCache = new LRUCache(2);<br>
lRUCache.put(1, 1); // cache is {1=1}<br>
lRUCache.put(2, 2); // cache is {1=1, 2=2}<br>
lRUCache.get(1);    // return 1<br>
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}<br>
lRUCache.get(2);    // returns -1 (not found)<br>
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}<br>
lRUCache.get(1);    // return -1 (not found)<br>
lRUCache.get(3);    // return 3<br>
lRUCache.get(4);    // return 4<br>


Constraints:<br>

- 1 <= capacity <= 3000
- 0 <= key <= 10<sup>4</sup>
- 0 <= value <= 10<sup>5</sup>
- At most 2 * 10<sup>5</sup> calls will be made to `get` and `put`.
<hr>

### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Any requirements on time/space complexity?<br>
2. Happy path
   ```
   LRUCache lRUCache = new LRUCache(3);
   lRUCache.put(1, 1); // cache is {1=1}
   lRUCache.put(2, 2); // cache is {1=1, 2=2}
   lRUCache.put(3, 3); // cache is {1=1, 2=2, 3=3}
   lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {2=2, 3=3, 4=4}
   lRUCache.get(1);    // returns -1 (not found)
   lRUCache.put(1, 1); // LRU key was 2, evicts key 2, cache is {3=3, 4=4, 1=1}
   lRUCache.get(2);    // return -1 (not found)
   lRUCache.get(3);    // return 3
   ```

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. LRU / Python's built-in OrderedDict
   - Use Python's built-in `OrderedDict` to implement an LRU(Least Recently Used) cache, which maintains insertion order and supports efficient reordering and deletion.
   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Use Python's `collections.OrderedDict` and function `move_to_end` and `popitem` to maintain a LRU(Least Recently Used) cache while inserting and deleting items.<br>

1) `from collections import OrderedDict`
2) In `class LRUCache`, we initialize `self.cache` as an `OrderedDict` object and `self.capacity = capacity`
3) In the definition of the function `get(self, key)`:
   - If `key` is in `self.cache`, use `move_to_end(key)` to mark it as recently used and return `self.cache[key]`
   - Otherwise, return `-1`
4) In the definitino of the function `put(self, key, value)`:
   - If `key` is in `self.cache`, update it and move to end using `move_to_end(key)`
   - If not, and if `len(self.cache) >= self.capacity`, evict the least recently used item using `popitem(last=False)`
   - Finally, insert or update the item with `self.cache[key] = value`
    
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume N is the specified capacity of the cache<br>

- Time Complexity: O(1)<br>
  Both `get` and `put` operations run in constant time because `OrderedDict` supports O(1) time complexity for key access, insertion, deletion, and reordering (`move_to_end`, `popitem`).<br>
- Space Complexity: O(N)<br>
  The space used grows linearly with the number of items stored, up to the specified capacity.
