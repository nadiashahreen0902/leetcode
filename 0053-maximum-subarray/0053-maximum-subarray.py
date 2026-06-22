class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        s=0
        for i in nums:
            s = s+i
            if s>ans:
                ans = s
            if s<0:
                s = 0
        return ans