def check(p1,p2,s):
    if p1>=p2:
        return "true"
    if(s[p1]!=s[p2]):
        return "false"
    return check(p1+1,p2-1,s)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans=""
        for i in s:
            if i.isalnum()==False:
                pass
            else:
                ans=ans+i
        ans=ans.lower()
        p1=0
        p2=len(ans)-1
        if(check(p1,p2,ans))=="true":
            return True
        else:
            return False
        