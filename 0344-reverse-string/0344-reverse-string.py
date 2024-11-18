class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        p1=0
        p2=len(s)-1
        self.reverse(s,p1,p2)
        print(s)
    def reverse(self,arr,p1,p2):
        if(p1>=p2):
            return
        arr[p1],arr[p2]=arr[p2],arr[p1]
        self.reverse(arr,p1+1,p2-1)
        