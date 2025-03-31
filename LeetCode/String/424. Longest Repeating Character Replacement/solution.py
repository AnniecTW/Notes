from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = Counter()
        res = 1
        i = 0

        for j in range(len(s)):
            freqs[s[j]] += 1
            maxFreq = max(freqs.values())
            curLen = j - i + 1
            if curLen - maxFreq > k:
                freqs[s[i]] -= 1
                i += 1
            res = max(res, j - i + 1)
        
        return res
