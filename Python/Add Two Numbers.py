# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self.int2linkList(self.linkList2int(l1) + self.linkList2int(l2))

    def linkList2int(self, l):
        result = 0
        times = 0
        while l != None:
            print l.val, result
            result += (l.val * (10 ** times))
            times += 1
            l = l.next
        return result

    def int2linkList(self, num):
        l = ListNode(num % 10)
        temp = l
        num /= 10
        while num > 0:
            temp.next = ListNode(num % 10)
            num /= 10
            temp = temp.next
        return l


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    app = Solution()
    print app.addTwoNumbers(l1, l2)
