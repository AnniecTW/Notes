from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        toMatch = len(need)
        minLength = float('inf')
        left = 0
        res = ""

        # use sliding window to track the smallest valid substring
        for right, char in enumerate(s):
            need[char] -= 1
            
            if need[char] == 0:
                toMatch -= 1
            
            while toMatch == 0:
                if right - left + 1 < minLength:
                    minLength = right - left + 1
                    res = s[left:right + 1]

                # try to shrink the window of substring from left
                need[s[left]] += 1
                if need[s[left]] == 1:
                    toMatch += 1
                left += 1

        return res
