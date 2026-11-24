# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next==None:
            return None
        dummy=ListNode()
        dummy.next=head
        k=0
        cur=dummy
        while k<n:
            cur=cur.next
            k+=1
        end=cur
        start=dummy
        while end.next:
            start=start.next
            end=end.next
        start.next=start.next.next
        return dummy.next
        
        