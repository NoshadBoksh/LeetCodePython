# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        
        # Helper: reverse a linked list between start and end (exclusive of end)
        def reverse(start, end):
            prev, curr = end, start
            while curr != end:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev  # new head after reversal

        # Dummy node to simplify head operations
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            # Find kth node from group_prev
            kth = group_prev
            for i in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next  # not enough nodes, return

            group_next = kth.next
            # Reverse the group
            start = group_prev.next
            new_head = reverse(start, group_next)

            # Reconnect
            group_prev.next = new_head
            start.next = group_next

            # Move group_prev for next round
            group_prev = start
