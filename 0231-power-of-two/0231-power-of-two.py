class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        val = 1
        for i in range(31):
            k = val<<i
            if k== n:
                return True
        return False
            
        