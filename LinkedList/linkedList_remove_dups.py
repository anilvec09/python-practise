# Merge Two Sorted Lists
# Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removedupslists(self, l1: ListNode):

        while l1 is not None:
            if l1.data == l1.next.data:
                l1.next == l1.next.next
             l1 = l1.next


