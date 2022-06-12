class Solution:
    def reverseString(self, s: List[str]) -> None:
        # Approach 1: With reverse() method
        s.reverse()
        
        # Time Complexity: O(n)
        # This algorithm uses O(n/2) means O(n)
        # Space Complexity: O(1)
        # No additional space is used
        
        # Approach 2: With left and right pointers
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] == s[right], s[left]
            left += 1
            right -= 1
            
        # Time Complexity: O(n)
        # This algorithm uses O(n/2) means O(n)
        # Space Complexity: O(1)
        # No additional space is used
