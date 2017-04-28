# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_num = []
        while l1:
            l1_num.insert(0, l1.val)
            l1 = l1.next
        l2_num = []
        while l2:
            l2_num.insert(0, l2.val)
            l2 = l2.next
        if len(l1_num) < len(l2_num):
            l1_num, l2_num = l2_num, l1_num
        c_in = 0
        length = len(l2_num)
        res = []
        for idx in xrange(length):
            two_sum = l1_num[idx] + l2_num[idx] + c_in
            res.append(two_sum % 10)
            c_in = 1 if two_sum > 9 else 0
        while len(l1_num) > length:
            two_sum = l1_num[length] + c_in
            res.append(two_sum % 10)
            c_in = 1 if two_sum > 9 else 0
            length += 1
        else:
            if c_in:
                res.append(c_in)
        node_list = [ListNode(x) for x in res[::-1]]
        for idx in xrange(len(node_list) - 1):
            node_list[idx].next = node_list[idx + 1]
        return node_list[0]
