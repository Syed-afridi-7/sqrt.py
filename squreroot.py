import math

class Solution:
    def mySqrt(self, x): 
        return int(math.sqrt(x))

n = 4 and 8
c = Solution()
ret = c.mySqrt(n)
print(ret)
