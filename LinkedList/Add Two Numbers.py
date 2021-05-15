# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = l1
        temp2 = l2
        l1_digits = []
        l2_digits = []
        while temp is not None:
            l1_digits.append(temp.val)
            temp = temp.next

        while temp2 is not None:
            l2_digits.append(temp2.val)
            temp2 = temp2.next
        l1_digits.reverse()
        l2_digits.reverse()
        print(l1_digits, l2_digits)
        l1_int = ''
        l2_int = ''
        for i in l1_digits:
            l1_int = l1_int + str(i)
        for i in l2_digits:
            l2_int = l2_int + str(i)
        print(l1_int, l2_int)

        tot_sum = str(int(l1_int) + int(l2_int))
        print(tot_sum)
        outputNode = None
        for i in range(0, len(tot_sum)):
            outputNode = ListNode(tot_sum[i], outputNode)
        return outputNode