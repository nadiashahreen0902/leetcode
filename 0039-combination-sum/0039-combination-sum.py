def comb(idx,target,l,ans,arr):
    if target == 0:  # Base case: target achieved
        ans.append(l[:])  # Append a copy of the valid combination
        return
    if idx == len(arr):  # Base case: no more elements
        return
    if (arr[idx]<=target):
        l.append(arr[idx])
        comb(idx,target-arr[idx],l,ans,arr)
        l.pop()
    comb(idx+1,target,l,ans,arr)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        l=[]
        ans=[]
        comb(0,target,l,ans,candidates)
        return ans
        
        