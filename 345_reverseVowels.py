class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        vowels = set("aeiouAEIOU")
        s = list(s)
        while l <= r:
            if l <= r and s[l] not in vowels:
                l += 1
            elif l <= r and s[r] not in vowels: 
                r -= 1 
            else:
                s[l], s[r] = s[r], s[l]
            
                l += 1
                r -= 1
        return "".join(s)
    
    # Space: O(1)
    # set data structure is implemented as a hash table 
    
    # Time: O(n)
    # I am traversing left and right towards the middle so each element is checked 
            
        
