# Given a linked list, remove the n-th node from the end of list and return its head.
#
# Example:
#
# Given linked list: 1->2->3->4->5, and n = 2.
#
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
#
# Given n will always be valid.
#
# Follow up:
#
# Could you do this in one pass?
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
### O(2N)
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    if head is None: return head

# SOLUTION 1 : TWO PASS , RUNTIME : 36 MS O(2N)
    temp = head
    count = 1
    list_len = 1
    while temp.next is not None:
        temp = temp.next
        list_len += 1

    temp = head
    while temp.next is not None:
        temp = temp.next
        count += 1
        if count == list_len - n:
            temp.next = temp.next.next
    return head

# SOLUTION 2 : ONE PASS , RUNTIME : 32 MS O(N)  , SPACE: O(1)
#         temp = head
#         count = 1
#         stack = []
#         while temp is not None:
#             stack.append(temp.val)
#             temp = temp.next
#             count += 1
#         stack.pop(-n)
#         stack.reverse()
#         print(stack)

#         newlist = None
#         for n in stack:
#             newlist = ListNode(n,newlist)

#         return newlist

# SOLUTION 3 : ONE PASS , RUNTIME : 52 MS O(2N)

#         temp, dummy, count = head, None, 0

#         while temp.next is not None:
#             temp = temp.next
#             count += 1
#             if count == n: dummy = head
#             if dummy and count != n: dummy = dummy.next
#             print(count,'    ',dummy)

#         if dummy is None:
#             head = head.next
#         else:
#             dummy.next = dummy.next.next

#         return head