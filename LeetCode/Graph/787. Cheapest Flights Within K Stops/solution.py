# optimized Dijkstra's algorithm
import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        # build graph: graph[from] = [(to, price)]
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        
        # (cost, src, stops)
        heap = [(0, src, 0)]
        
        # record visited (node, stops) 
        visited = dict()

        while heap:
            cost, city, stops = heapq.heappop(heap)

            if city == dst:
                return cost

            if (city, stops) in visited and visited[(city, stops)] <= cost:
                continue
            visited[(city, stops)] = cost

            if stops > k:
                continue

            for neighbor, price in graph[city]:
                heapq.heappush(heap, (cost + price, neighbor, stops + 1))
        
        return -1
