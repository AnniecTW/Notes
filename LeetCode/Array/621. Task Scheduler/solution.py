from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        maxFreq = max(counter.values())

        # how many tasks that are most freqent
        max_count = sum(1 for freq in counter.values() if freq == maxFreq)

        # fill with other tasks or idle times
        min_len = (maxFreq - 1) * (n + 1) + max_count

        return max(min_len, len(tasks))
