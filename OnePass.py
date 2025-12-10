# Definition for singly linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head

        fast = dummy
        slow = dummy

        # Move fast n steps ahead
        for _ in range(n):
            fast = fast.next

        # Move together until fast reaches the last node
        while fast.next:
            fast = fast.next
            slow = slow.next

        # slow.next is the node to remove
        slow.next = slow.next.next

        return dummy.next
