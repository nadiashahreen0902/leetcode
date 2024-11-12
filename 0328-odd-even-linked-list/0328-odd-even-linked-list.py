# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyeve = ListNode(100000)
        dummyodd = ListNode(100000)
        actualodd = dummyodd
        actualeve = dummyeve
        pos=0
        temp=head
        while(temp != None):
            pos+=1
            print(pos)
            if pos%2!=0:
                dummyodd.next = temp
                dummyodd= dummyodd.next
            elif(pos%2==0):
                dummyeve.next = temp
                dummyeve = dummyeve.next
            temp = temp.next
        print(dummyeve)
        dummyeve.next= None
        actualodd1= actualodd.next
        actualeve1= actualeve.next
        dummyodd.next = actualeve1
        return(actualodd1)
        