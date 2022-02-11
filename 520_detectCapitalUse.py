n = len(word)
        # Approach - 1: Checking chars by chars
        
        if len(word) == 1:
            return True
        
        if word[0].isupper() and word[1].isupper():
            for i in range(2,n):
                if not word[i].isupper():
                    return False
        else:
            for i in range(1,n):
                if word[i].isupper():
                    return False
        return True
        
#         Time Complexity: O(n) 
#         Checking chars by chars in the length of word
        
#         Space Complexity: O(1)
#         Using constant spaces to store variables
