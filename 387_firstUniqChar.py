class Solution:
    def firstUniqChar(self, s: str) -> int:
        count_s = collections.Counter(s)
        
        for ind, val in enumerate(s):
            if count_s[val] == 1:
                return ind
        return -1
