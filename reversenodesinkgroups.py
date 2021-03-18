from pdb import set_trace

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        def reverseStartEnd(start, end, n):
            if n == 1:
                return start
            
            incrementer = start
            tmp_container = []
            
            for i in range(n):
                tmp_container.append(incrementer)
                incrementer = incrementer.next
            
            #print('display sub group:')
            
            for i in reversed(range(1,n)):
                #print(tmp_container[i].val)
                tmp_container[i].next = tmp_container[i-1]
            tmp_container[0].next = None

            return tmp_container[n-1]

        segments = []
        incrementer = head
        count = 0
        #set_trace()
        while True:
            if count % k == 0:
                start = incrementer
            if count % k == k-1:
                end = incrementer
                #print((start.val, end.val))
                segments.append([start, end])
            incrementer = incrementer.next    
            count += 1
            if incrementer is None:
                break
        
        number_of_segments = count // k
        
        if number_of_segments == 0:
            return head
        
        reverse_segments = []
        for pair in segments:
            new_start = reverseStartEnd(pair[0], pair[1], k)
            #print(f"reversed end: {new_start.next.val}")
            reverse_segments.append([new_start,pair[0]])
        
        #print('reached here?')
        for i in range(number_of_segments-1):
            reverse_segments[i][1].next = reverse_segments[i+1][0]
            #print(f"end: start -> {reverse_segments[i][1].val} -> {reverse_segments[i+1][0].val}")
        if count % k != 0:
            reverse_segments[number_of_segments-1][1].next = start
        #print(f"start val is: {incrementer.val}")
        
        return reverse_segments[0][0]

if __name__ == '__main__':
    test = [1,2]
    lists = [ListNode(i) for i in test]
    for i in range(len(test)-1):
        lists[i].next = lists[i+1]

    #head = lists[0]
    #while head is not None:
    #    print(head.val)
    #    head = head.next
    sol = Solution()
    result = sol.reverseKGroup(lists[0],2)
    while result is not None:
        print(result.val)
        result = result.next
