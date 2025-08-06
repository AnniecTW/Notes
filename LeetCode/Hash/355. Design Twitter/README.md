## 355. Design Twitter
🔗 Link: [Design Twitter](https://leetcode.com/problems/design-twitter/description/)<br>
💡 Difficulty: Medium<br>
🛠️ Topics: Hash Table / Heap<br>

<hr>
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the `10` most recent tweets in the user's news feed.<br>

Implement the `Twitter` class:<br>

- `Twitter()` Initializes your twitter object.
- `void postTweet(int userId, int tweetId)` Composes a new tweet with ID `tweetId` by the user `userId`. Each call to this function will be made with a unique `tweetId`.
- `List<Integer> getNewsFeed(int userId)` Retrieves the `10` most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
- `void follow(int followerId, int followeeId)` The user with ID followerId started following the user with ID `followeeId`.
- `void unfollow(int followerId, int followeeId)` The user with ID followerId started unfollowing the user with ID `followeeId`.

Example 1:<br>

> Input<br>
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]<br>
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]<br>
Output<br>
[null, null, [5], null, null, [6, 5], null, [5]]<br>

> Explanation<br>
Twitter twitter = new Twitter();<br>
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).<br>
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]<br>
twitter.follow(1, 2);    // User 1 follows user 2.<br>
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).<br>
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.<br>
twitter.unfollow(1, 2);  // User 1 unfollows user 2.<br>
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.<br>


Constraints:<br>

- 1 <= userId, followerId, followeeId <= 500
- 0 <= tweetId <= 10<sup>4</sup>
- All the tweets have unique IDs.
- At most 3 * 10<sup>4</sup> calls will be made to `postTweet`, `getNewsFeed`, `follow`, and `unfollow`.
- A user cannot follow himself.
<hr>

### UMPIRE Method:
#### Understand

> - Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
> - Choose a “happy path” test input, different than the one provided, and a few edge case inputs. 
> - Verify that you and the interviewer are aligned on the expected inputs and outputs.
1. Any requirements on time/space complexity?<br>
2. Happy path
   ```java
   Twitter twitter = new Twitter();
   twitter.postTweet(1, 4); // User 1 posts a new tweet (id = 4).
   twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
   twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet id -> [4, 5]. return [5, 4]
   twitter.follow(1, 2);    // User 1 follows user 2.
   twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
   twitter.getNewsFeed(1);  // User 1's news feed should return a list with 3 tweet ids -> [6, 5, 4]. 
   twitter.unfollow(1, 2);  // User 1 unfollows user 2.
   twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5, 4], since user 1 is no longer following user 2.
   ```

### Match
> - See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category
1. Hash Table
   - Use a dictionary to record the tweet posted with the corresponding timestamp and userID
   - Use another dictionay to record the followees of a user
2. Heap (Priority Queue)
   - In `getNewsFeed()`, we use a heap to proritize posts (at most 10 recent posts from each followee) based on its timestamp
   
### Plan
> - Sketch visualizations and write pseudocode
> - Walk through a high level implementation with an existing diagram

General Idea: Use dictionaries to record the tweets and follow relationships. Then we use max heap to prioritize tweets from followees by timestamp.<br>

1) import modules:
   ```python
   from collections import defaultdict
   import heapq
   ```
2) Initiailize class:
   ```python
   class Twitter:

     def __init__(self):
        self.tweets = defaultdict(list) # Dictionary to record tweets
        self.followeeId = defaultdict(set) # Dictionary to record followees
        self.ts = 0 # timestamp to get the latest posts
   ```
3) In the definition of the function `postTweet(self, userId: int, tweetId: int)`:
   ```python
   def postTweet(self, userId: int, tweetId: int) -> None:
       self.tweets[userId].append((-self.ts, tweetId))
       self.ts += 1
   ```
4) In the definitino of the function `getNewsFeed(self, userId: int)`:
   ```python
   maxHeap = []
   followees = self.followeeId[userId] | {userId}
   for user in followees:
       for ts, tweetId in self.tweets[user][-10:]:
           heapq.heappush(maxHeap, (ts, tweetId)) # get the latest 10 tweets from each followees (including self)

   res = []
   while maxHeap and len(res) < 10:
       res.append(heapq.heappop(maxHeap)[1]) # get the latest 10 tweets from heap pools according to timestamp
   
   return res
   ```
5) In the definitino of the function `follow(self, followerId: int, followeeId: int)` and `unfollow(self, followerId: int, followeeId: int)`:
   ```python
   def follow(self, followerId: int, followeeId: int) -> None:
       self.followeeId[followerId].add(followeeId)

   def unfollow(self, followerId: int, followeeId: int) -> None:
       self.followeeId[followerId].discard(followeeId)
   ```
    
### Implement
> - Implement the solution (make sure to know what level of detail the interviewer wants)

see solution.py

### Review
> - Re-check that your algorithm solves the problem by running through important examples
> - Go through it as if you are debugging it, assuming there is a bug
### Evaluate
> - Finish by giving space and run-time complexity
> - Discuss any pros and cons of the solution

Assume F is the number of followees (including self) and T is the numbers of total tweets

- Time Complexity: O(N)<br>
  - `postTweet`: O(1)
  - `follow` / `unfollow`: O(1)
  - `getNewsFeed`: O(F * log(F * 10)) = O(F * log F)
    - For each followee (including self), we retrieve at most 10 recent tweets.
    - So at most F × 10 tweets are pushed to the `maxHeap`.
    - Each push/pop operation costs at most O(log F × 10).
    - So, the total time is O(F × log F)
- Space Complexity: O(T + F)<br>
  - `self.tweets`: O(T)
  - `self.followeeId`: O(F)
  - In `getNewsFeed`, the maxHeap stores at most F × 10 items: O(F)
  - Overall: O(T + F)
