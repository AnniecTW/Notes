## 121. Best Time to Buy and Sell Stock
🔗 Link: [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)<br>
💡 Difficulty: Easy<br>
🛠️ Topics: Array<br>

=======================================================================================<br>

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`<sup>`th`</sup> day.<br>

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.<br>

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.<br>

 

Example 1:<br>

Input: prices = [7,1,5,3,6,4]<br>
Output: 5<br>
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.<br>
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.<br>

Example 2:<br>

Input: prices = [7,6,4,3,1]<br>
Output: 0<br>
Explanation: In this case, no transactions are done and the max profit = 0.<br>
 

Constraints:<br>

- 1 <= prices.length <= 105<br>
- 0 <= prices[i] <= 104<br>

=======================================================================================<br>
### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Can the array `prices` be empty?
- No, the length of an array is restricted to be greater than or equal to 1, so there must be at least one element in the array, and the array cannot be empty.
2. In this case, is short selling or day trading possible?
- No, buying must be before selling.
3. Happy cases<br>  Input: prices = [10,2,5] ; Output: 3<br>
4. Are there any time or space complexity I should be aware of?
- An optimal solution would have O(n) in time complexity and O(1) in space complexity

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. Array<br>
The main task is to perform calculations or operations on the given array.

### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General idea: Traverse the entire list and store the smallest value in a variable `buy_price`. While traversing, calculate the difference between the current price and `buy_price` and store it in a variable `profit`. Finally, obtain the maximum `profit`. <br>

1) Initiate variables `buy_price = prices[0]` 、 `profit = 0`.<br>

2) Traverse the list from second element to the end and store the smallest value in a variable `buy_price`.<br>
    
3) While traversing, calculate the difference between the current price and `buy_price` and store it in a variable `profit`.<br>
   - Since `buy_price` is stored fisrt, any subsequent prices encountered will appear after `buy_price`, ensuring that selling never occurs before buyinhg.
    
4) During each traversal, update `profit` if a higher value is found. <br>

5) Return `profit`. <br>

### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity

Assume N is the length of the input array `prices`.


- Time Complexity: O(N)
- Space Complexity: O(1)
