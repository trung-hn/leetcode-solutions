#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# TAGS: Linked List, Two Pointers
# REVIEWME: Linked List
import collections
class Solution:
    # 36 ms, 77.37%. Time: O(N). Space: O(1)
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head: return head
        
        # Find length of list
        node = head
        L = 0
        while node:
            L += 1
            node = node.next
        
        # Reduce k
        k %= L
        if k == 0: return head
        
        node = head
        prev = None
        for i in range(L):
            prev = node
            node = node.next
            if i == L - k - 1:
                rv = prev.next
                prev.next = None
        prev.next = head
        return rv
    
    # 32 ms, 92.87%. Similar to above but Break it out. Time: O(N). Space: O(1)
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head: return head
        
        # Find length of list
        L = 0
        node = head
        while node:
            L += 1
            node = node.next
        
        # Reduce k
        k %= L
        if k == 0: return head
        
        # Find new tail and point it to None
        node = head
        prev = None
        for _ in range(L - k):
            prev = node
            node = node.next
        prev.next = None

        # This is new head
        rv = node

        # Point last node back to first node
        prev = None
        while node:
            prev = node
            node = node.next
        prev.next = head
        return rv
        
# @lc code=end

