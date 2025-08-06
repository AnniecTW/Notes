from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followeeId = defaultdict(set)
        self.ts = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-self.ts, tweetId))
        self.ts += 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        followees = self.followeeId[userId] | {userId}
        for user in followees:
            for ts, tweetId in self.tweets[user][-10:]:
                heapq.heappush(maxHeap, (ts, tweetId))

        res = []
        while maxHeap and len(res) < 10:
            res.append(heapq.heappop(maxHeap)[1])
        
        return res
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followeeId[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followeeId[followerId].discard(followeeId)
