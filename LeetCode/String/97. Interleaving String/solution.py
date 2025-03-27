class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n3 != n1 + n2:
            return False
        
        # use dp to represent whether s1[:i] and s2[:j] can form s3[:i+j]
        dp = [[False] * (n2 + 1) for _ in range(n1 + 1)]
        dp[0][0] = True

        for i in range(1, n1 + 1):
            dp[i][0] = s1[i-1] == s3[i-1] and dp[i-1][0]

        for j in range(1, n2 + 1):
            dp[0][j] = s2[j-1] == s3[j-1] and dp[0][j-1]

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                dp[i][j] = (s1[i-1] == s3[i+j-1] and dp[i-1][j]) or (s2[j-1] == s3[i+j-1] and dp[i][j-1])


        return dp[n1][n2]


            
