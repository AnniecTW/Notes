from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = defaultdict(list)
        for s in strs:
            dictionary[''.join(sorted(s))].append(s)
        return list(dictionary.values())
