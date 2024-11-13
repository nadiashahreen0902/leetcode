# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        x = head
        hs = set()
        while(x!=None):
            if x not in hs:
                hs.add(x)
            elif(x in hs):
                return True
                break
            x=x.next
        return False
            
            
        