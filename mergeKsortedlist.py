# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue
import heapq
class Solution:
    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        #q = PriorityQueue()
        #start = ListNode()
        #result = start
        #print(result.val)
    
        #for count, lst in enumerate(lists):
           #print(lst.val)
        #   if lst:
        #        q.put((lst.val, count, lst))
        
        #while not q.empty():
        #    value, count, node = q.get()
        #    start.next = ListNode(value)
        #    start = start.next
        #    node = node.next
        #    if node:
        #        q.put((node.val, count, node))
        
        #return result.next
    
        result = []
        start = rtnnode = ListNode()
        
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(result, (lst.val,i, lst))
        
        while result:
            value,i, node = heapq.heappop(result)
            start.next = node
            start = start.next
            node = node.next
            if node:
                heapq.heappush(result, (node.val, i, node))
            
        return rtnnode.next
