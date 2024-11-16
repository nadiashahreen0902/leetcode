class Solution:
    def largestOddNumber(self, num: str) -> str:
        idx=""
        for i in range(len(num)-1,-1,-1):
            if int(num[i])%2!=0:
                idx = i
                break
        if idx == "":
            return idx
        else:
            return num[:idx+1]
                
                
                