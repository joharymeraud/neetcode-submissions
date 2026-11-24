# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None:
            return list2
        if list2==None:
            return list1
        cur1=list1
        cur2=list2
        if list1.val<list2.val:head,tail,cur1=list1,cur1,cur1.next
        else:head,tail,cur2=list2,cur2,cur2.next
        while cur1!=None and cur2!= None:
            if cur1.val<=cur2.val:
                tail.next=cur1
                tail=tail.next
                cur1=cur1.next
            else:
                tail.next=cur2
                tail=tail.next
                cur2=cur2.next
        if cur1==None:
            tail.next=cur2
        else:
            tail.next=cur1         
        return head
        