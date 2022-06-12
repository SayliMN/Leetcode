class Solution:
    def isValid(self, s: str) -> bool:
        bracket_mapping = {
                '}':'{',
                ']':'[',
                ')':'('
            }
        stack = []

        for bracket in s:
            if bracket in bracket_mapping:
                if stack and stack[-1] == bracket_mapping[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)

        return True if not stack else False
    
    # Time: O(n)
    # Space: O(n)
