class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans=0
        l=[]
        n = len(nums)//3
        hm=dict()
        for i in nums:
            hm[i]=0
        for i in nums:
            hm[i]+=1
        for i in nums:
            ans = max(hm[i],ans)
        for k in hm:
            if hm[k]>n:
                l.append(k)
        return l
                
            