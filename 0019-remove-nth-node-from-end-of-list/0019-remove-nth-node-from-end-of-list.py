# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        temp = reverse(head)
        prev= temp
        main = temp
        if n ==1:
            prev = prev.next
            temp.next = None
            return(reverse(prev))        
        else:
            for i in range(n-2):
                temp = temp.next
            temp.next = temp.next.next
            return(reverse(main))
def reverse(curr):
    prev = None
    while(curr != None):
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev



        