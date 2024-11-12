class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head.next== None:
            return True
        else:
            m1 = head
            m = mid(head)
            m2 = m.next
            m.next = None
            m2 = reverse(m2)
            f=0
            while(m1 != None and m2 != None):
                if m1.val == m2.val:
                    f=0
                else:
                    f=1
                    break
                m1=m1.next
                m2=m2.next
            if f==0:
                return True
            else:
                return False    
def mid(curr):
    if curr == None:
        return curr
    s=curr
    f=curr
    while(f.next != None and f.next.next!=None):
        s=s.next
        f=f.next.next
    return s
def reverse(cur):
    prev = None
    while(cur != None):
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return prev
        
            
            