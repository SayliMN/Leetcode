        # Two pointers solution
        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
        
#         Time complexity: O(n)
#         I traverse over each character at most once, until the left and the right pointers meet in the middle.
        
#         Space complexity: O(1)
#         No extra space is required
