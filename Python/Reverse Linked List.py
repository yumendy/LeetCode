# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if head == None:
            return head
        elif head.next == None:
            return head
        start = head
        temp = head.next
        start.next = None
        while temp.next:
            prev = head
            head = temp
            temp = temp.next
            head.next = prev
        temp.next = head
        return temp