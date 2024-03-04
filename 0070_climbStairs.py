class Solution:
    def climbStairs(self, n: int) -> int:
        if 0 < n <= 2:
            return n
        
        first = 1
        second = 2
        third = 0
        for i in range(3, n+1):
            third = first + second
            first = second
            second = third
        return second
    
    # O(n),O(1)
        
#         if n <= 2:
#             return n
        
#         dp = [0]*(n+1)
#         dp[1], dp[2] = 1,2
#         for i in range(3,n+1):
#             dp[i] = dp[i-1] + dp[i-2]
#         return dp[i]
#     # O(n),O(n)
            
       
            
