from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        count_s1 = Counter(s1)
        count_s2 = Counter(s2[:len(s1)])
        if count_s1 == count_s2:
                return True

        i, j = 0, len(s1) - 1

        while j < len(s2) - 1:
            j += 1
            count_s2[s2[j]] += 1
            count_s2[s2[i]] -= 1
            if count_s2[s2[i]] == 0:
                del count_s2[s2[i]]
            i += 1

            if count_s1 == count_s2:
                return True
        return False
            
