# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head
        while cur:
            nxt = cur.next      # sauvegarder la suite avant 
            cur.next = prev     # retourner la flèche
            prev = cur          # avancer prev
            cur = nxt           # avancer cur
        return prev  

    def middleNode(self,head):
        slow=head
        fast=head
        while fast and fast.next and fast.next.next:
            fast=fast.next.next
            slow=slow.next
        return slow       
    def reorderList(self, head: Optional[ListNode]) -> None:

        mid=self.middleNode(head) 

        beginsec=mid.next
        mid.next=None

        end=self.reverseList(beginsec)
        start=head

        while start.next:

            nxtst=start.next
            start.next=end
            start=nxtst

            nxtend=end.next
            end.next=start
            end=nxtend
        if end: start.next=end
        





        
            


        
        
        