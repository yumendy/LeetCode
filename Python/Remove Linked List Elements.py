# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        if head != None:
            while(head.val == val):
                head = head.next
                if head is None:
                    return None
            temp = head
            while temp.next is not None:
                if temp.next.val == val:
                    temp.next = temp.next.next
                else:
                    temp = temp.next
        return head