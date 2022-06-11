class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary = {
            "I" : 1,
            "IV" : 4,
            "V" : 5,
            "IX" : 9,
            "X" : 10,
            "XL" : 40,
            "L" : 50,
            "XC" : 90,
            "C" : 100,
            "CD" : 400,
            "D" : 500,
            "CM" : 900,
            "M" : 1000    
        }
        total, i = 0, 0
        while i < len(s):
            if s[i:i+2] in dictionary:
                total += dictionary[s[i:i+2]]
                i += 2
            else:
                total += dictionary[s[i]]
                i += 1     
        return total
    
    # O(1),O(1) --> finite values are maintained in dictionary, also the constraint to convert is lesser than equals to 3999
