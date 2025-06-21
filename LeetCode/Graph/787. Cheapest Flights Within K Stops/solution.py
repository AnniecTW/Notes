from collections import defaultdict, deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        cost = [float('inf') for _ in range(n)] # record the lowest cost from src to dst within k stops
        cost[src] = 0

        for s, d, p in flights:
            graph[s].append((d, p))

        queue = deque([(0, src, 0)]) # price, node, stops
        while queue:
            price, node, stops = queue.popleft()

            if stops > k:
                break

            for d, p in graph[node]:
                if cost[d] > p + price:
                    cost[d] = p + price
                    queue.append((p + price, d, stops + 1))
        
        return -1 if cost[dst] == float('inf') else cost[dst]
