# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val1 = ''
        val2 = ''
        while(l1!=None):
            val1 = str(l1.val) + val1
            l1 = l1.next
        while(l2!=None):
            val2 = str(l2.val) + val2
            l2 = l2.next

        addition = int(val1) + int(val2)
        l1 = ListNode(0, None)
        l1.val = addition%10
        addition = addition/10
        l2=l1

        while addition>0:
            l1.next = ListNode(0, None)
            l1 = l1.next
            l1.val = addition%10
            addition = addition/10

        return l2
