class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for i in ops:
            if i not in "+DC":
                stack.append(int(i))
            elif i == "C":
                stack.pop()
            elif i == "D":
                stack.append(stack[-1] * 2)
            elif i == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                break
                
        return sum(stack)
    
    # O(N),O(N)
                
