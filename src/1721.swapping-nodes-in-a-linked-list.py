#
# @lc app=leetcode id=1721 lang=python3
#
# [1721] Swapping Nodes in a Linked List
#

# @lc code=start
# TAGS: Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 1100 ms, 69.17%. Time: O(N). Space: O(1)
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        L = 0
        node = head
        while node:
            L += 1
            node = node.next
                    
        i = 0
        node = head
        while node:
            if i == k - 1:node1 = node
            if i == L - k: node2 = node
            i += 1
            node = node.next
            
        node1.val, node2.val = node2.val, node1.val
        return head
        
    # 1 pass. 1060 ms, 82.58%. Time: O(N). Space: O(1)
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        n1 = n2 = None
        node = head
        while node:
            k -= 1
            if n2: n2 = n2.next
            if k == 0:
                n1 = node
                n2 = head
            node = node.next
        n1.val, n2.val = n2.val, n1.val
        return head
# @lc code=end

