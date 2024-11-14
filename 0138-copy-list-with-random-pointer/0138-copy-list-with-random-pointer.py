"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head==None:
            return head
        curr =head
        while(curr):
            nn = Node(curr.val)
            nn.next = curr.next
            curr.next = nn
            curr=nn.next
        curr = head
        while(curr):
            if curr.random:
                curr.next.random = curr.random.next
            curr =curr.next.next
        c1=head
        c2=head.next
        ans=head.next
        while c1.next and c2.next:
            c1.next = c2.next
            c2.next=c1.next.next
            c1=c1.next
            c2=c2.next
        return(ans)
            
        