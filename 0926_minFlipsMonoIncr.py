class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        flipped_zeros = s.count("0")
        ones_to_zeros = 0
        result = flipped_zeros
        for c in s:
            flipped_zeros -= c == '0'
            ones_to_zeros += c == '1'
            result = min(result, flipped_zeros+ones_to_zeros)
        return result
    
    # Time= O(n)
    # Space: O(1)
