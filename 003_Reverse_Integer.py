class Solution:
    def reverse(self, x: int) -> int:
        min_val = -1 * 2**31
        max_val = 2**31 - 1
        if x >= 0:
            a = int(str(x)[::-1])
        if x < 0:
            a = -1 * int(str(x*-1)[::-1])
        
        if a not in range(min_val, max_val):
            return 0
        else:
            return a
        
#         if x >= 0:
#             return int(''.join(reversed(str(x))))
#         else:
#             return int('-'+''.join(reversed(str(x*-1))))
