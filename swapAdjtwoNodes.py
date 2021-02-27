# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if not head:
            return None
        if head.next is None:
            return head
        
        start = head
        start_next = start.next
        end = start_next
        
        while start is not None:
            if start_next is None:
                return end
            tmp = start_next.next
            start_next.next = start
            if tmp is None or tmp.next is None:
                start.next = tmp
            else:
                start.next = tmp.next
            
            start = tmp
            if start is not None and start.next is not None:
                start_next = start.next
            else:
                start_next = None
            
        return end
