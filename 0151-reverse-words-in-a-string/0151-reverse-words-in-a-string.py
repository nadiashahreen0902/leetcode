class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        ans=""
        for i in range(len(l)-1,-1,-1):
            ans= ans+l[i]
            if i!=0:
                ans = ans+" "
        
        return(ans)
            
            
        
        