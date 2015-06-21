# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if head is None:
            return None
        elif head.next is None:
            return head
        else:
            temp = head
            while temp.next:
                if temp.val == temp.next.val:
                    temp.next = temp.next.next
                else:
                    temp = temp.next
        return head