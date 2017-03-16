# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        elif not l2:
            return l1
        else:
            a = l1
            b = l2
            result = last = None
            while 1:
                while a and a.val < b.val:
                    if not result:
                        result = last = a
                        a = a.next
                    else:
                        last.next = a
                        last = last.next
                        a = a.next
                        if a is None:
                            break
                if a is None:
                    last.next = b
                    break
                while b and a.val >= b.val:
                    if not result:
                        result = last = b
                        b = b.next
                    else:
                        last.next = b
                        last = last.next
                        b = b.next
                        if b is None:
                            break
                if b is None:
                    last.next = a
                    break
            return result
