# Approach 1: 
        
        return ' '.join(s.split()[::-1])[::-1]
    
        # Appraoch 2: with for loop
        
        return ' '.join(x[::-1] for x in s.split())
    
        # Time Complexity: O(n*2)
        # Space Complexity: O(1)
  

 # Approach 2: Sliding window
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
  def reverseWords(self, s: str) -> str:      
     result = ""
     chars = 0
     for i, char in enumerate(s):
        if char != " ":
           chars += 1
        else:
           result += " " if result else ""
           k = i - 1
           while(chars):
              result += s[k]
              chars -= 1
              k -= 1
     result += " " if result else ""   
     while(chars):
        result += s[i]
        chars -= 1
        i -= 1
     return result
          
             
        
