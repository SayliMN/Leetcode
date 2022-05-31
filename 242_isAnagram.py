class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return collections.Counter(s) == collections.Counter(t)
        # Time Complexity: O(n)
        # Space Complexity: O(1) --> at max 26 alphabets 
        
        dictionary = {}
        for i in s:
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1
                
        for j in t:
            if j in dictionary: 
                dictionary[j] -= 1
            else:
                return False
            
        for val in dictionary.values():
            if val != 0:
                return False
            
        return True
