# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        dic = {None:None}
        temp = head
        while temp:
            dic[temp] = RandomListNode(temp.label)
            temp = temp.next
        temp = head
        while temp:
            dic[temp].next = dic[temp.next]
            dic[temp].random = dic[temp.random]
            temp = temp.next
        return dic[head]        
