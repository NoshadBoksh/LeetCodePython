# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq   # we need Python's built-in min-heap

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        # Step 1: Initialize a heap
        heap = []
        
        # Step 2: Put the head of each non-empty list into the heap
        # We store (node value, index, node) because ListNode itself is not directly comparable
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        # Step 3: Create a dummy head for the result list
        dummy = ListNode(0)
        current = dummy
        
        # Step 4: Keep extracting the smallest node from the heap
        while heap:
            val, i, node = heapq.heappop(heap)  # get smallest
            current.next = node                 # append to result list
            current = current.next              # move forward
            
            if node.next:  # push the next node from this list
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        # Step 5: Return merged list (skipping dummy head)
        return dummy.next
