# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        fast, slow = head.next, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        half = slow.next
        slow.next = None
        
        temp = None
        while half:
            nxt = half.next
            half.next = temp
            temp = half
            half = nxt
        
        while temp:
            if head.val != temp.val:
                return False
            head = head.next
            temp = temp.next
        return True
