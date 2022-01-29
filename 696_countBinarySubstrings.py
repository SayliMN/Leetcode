class Solution:
    def countBinarySubstrings(self, s: str) -> int:
      prev, cur, ans = 0, 1, 0
      for i in range(1,len(s)):
          if s[i-1] != s[i]:
              ans += min(prev,cur)
              prev, cur = cur, 1
          else:
              cur += 1

      return ans + min(prev,cur)
#      Time complexity: O(n)
#      Space complexity: O(1)

#         groups = [1]
#         for i in range(1,len(s)):
#             if s[i-1] != s[i]:
#                 groups.append(1)
#             else:
#                 groups[-1] += 1
        
#         result = 0
#         for j in range(1,len(groups)):
#             result += min(groups[j-1], groups[j])
#         return result
#      Time complexity: O(n)
#      Space complexity: O(n)
