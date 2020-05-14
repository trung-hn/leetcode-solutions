#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# TAGS: Linked List, 
class Solution:
        # 36 ms, 69.35%. Time: O(N). Space: O(1)
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = node = ListNode(0)
        while l1 and l2:
            if l1.val > l2.val:
                node.next = ListNode(l2.val)
                l2 = l2.next
            else:
                node.next = ListNode(l1.val)
                l1 = l1.next
            node = node.next
        if l1: node.next = l1
        if l2: node.next = l2
        return head.next
        
# @lc code=end

