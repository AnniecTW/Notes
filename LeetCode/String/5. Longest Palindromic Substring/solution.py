class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        def fromcenter(s: str, left: int , right: int):
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right

        l, r = 0, 0

        for i in range(len(s)):
            odd_l, odd_r = fromcenter(s, i, i)
            even_l, even_r = fromcenter(s, i, i+1)
            l, r = max((odd_l, odd_r), (even_l, even_r), (l, r), key=lambda x: (x[1] - x[0]))
        return s[l:r]
