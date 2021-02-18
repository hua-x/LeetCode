# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if not l1:
            return l2
        elif not l2:
            return l1
        
        marker1 = l1
        marker2 = l2
        
        if marker1.val < marker2.val :
            result = marker1
            marker1 = marker1.next
        else:
            result = marker2
            marker2 = marker2.next
        
        return_value = result
        
        while marker1 and marker2:
            if marker1.val < marker2.val:
                result.next = marker1
                marker1 = marker1.next
            else:
                result.next = marker2
                marker2 = marker2.next
            result = result.next
            
        if marker1:
            result.next = marker1
        else:
            result.next = marker2
            
        return return_value
            
                
