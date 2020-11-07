#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#

# @lc code=start
# TAGS: Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 72 ms, 72.55%. Time and Space: O(N)
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def get_num(node):
            rv = 0
            while node:
                rv = (rv * 10) + node.val
                node = node.next
            return rv
        
        root = node = ListNode()
        num = get_num(l1) + get_num(l2)
        num_len = len(str(num)) - 1
        while num_len > -1:
            digit = (num // (10**num_len)) % 10
            num_len -= 1
            node.next = ListNode(digit)
            node = node.next
        return root.next
    
    # 64 ms, 96.54%. Time and Space: O(N)
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverse_list(node):
            prev = None
            while node:
                tmp = node.next
                node.next = prev
                prev = node
                node = tmp
            return prev
        l1 = reverse_list(l1)
        l2 = reverse_list(l2)
        
        root = node = ListNode()
        carry = 0
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, rem = divmod(v1 + v2 + carry, 10)
            node.next = ListNode(rem)
            node = node.next
        return reverse_list(root.next)
# @lc code=end

