class Solution:
    def fib(self, n: int) -> int:
        #iterative bottom up approach
        if n <= 1:
            return n
        curr = 0
        prev_1 = 1
        prev_2 = 0
        for i in range(2,n+1):
            curr = prev_1 + prev_2
            prev_2 = prev_1
            prev_1 = curr
        return curr
    
        prev_1, prev_2 = 0, 1
        for _ in range(n):
            prev_1, prev_2 = prev_2, prev_1 + prev_2
        return prev_1
    
    # O(n), O(1)
