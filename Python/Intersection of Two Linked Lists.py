# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if (not headA) or (not headB):
            return None
        temp = headB
        while temp.next:
            temp = temp.next
        temp.next = headB
        fast = slow = headA
        res = None
        while fast and slow:
            fast = fast.next
            slow = slow.next
            if fast:
                fast = fast.next
            if fast == slow:
                break
        if fast and slow and fast == slow:
            slow = headA
            while fast != slow:
                fast = fast.next
                slow = slow.next
            res = slow

        temp.next = None
        return res
