class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        i, longest = 0, 0 

        for j in range(len(s)):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            
            seen.add(s[j])
            longest = max(longest, j - i + 1)

        return longest
