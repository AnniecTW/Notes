from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i, j, n = 0, 0, len(s)
        counter = Counter()
        longest = float('-inf')

        while j < n:
            counter[s[j]] += 1
            max_freq = max(counter.values())
            str_length = j - i + 1
            while str_length - max_freq > k:
                counter[s[i]] -= 1
                i += 1
                max_freq = max(counter.values())
                str_length = j - i + 1

            longest = max(longest, j - i + 1)
            j += 1    

        return longest
