# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        start = head
        count = 1
        target = None
        if start.next is None:
            return None
        
        while start.next is not None :
            start = start.next
            count += 1
            if count == 1 + n:
                target = head
            elif count > 1 + n:
                target = target.next
        
        if not target:
            return head.next
        else:
            target.next = target.next.next
        
        return head
