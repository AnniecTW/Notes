from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = [(0, k)] # (distance, node)
        dist = [float('inf') for _ in range(n + 1)]
        dist[k] = 0

        # build adjacency list
        adjacency = defaultdict(list)
        for src, dst, time in times:
            adjacency[src].append((dst, time))

        # Dijkstra algo
        while heap:
            shortest, node = heapq.heappop(heap)
            if shortest > dist[node]:
                continue
            
            for dst, time in adjacency[node]:

                if shortest + time < dist[dst]:
                    dist[dst] = shortest + time

                    heapq.heappush(heap, (dist[dst], dst))

        res = max(dist[1:])
        return -1 if res == float('inf') else res
