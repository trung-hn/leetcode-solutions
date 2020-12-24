#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# TAGS: Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 24 ms, 94.63%. Time: O(N). Space: O(N)
    def swapPairs(self, head: ListNode) -> ListNode:
        def dfs(node):
            if not node or not node.next: return node
            cur = node
            nxt = node.next
            cur.next = dfs(nxt.next)
            nxt.next = cur
            return nxt
        return dfs(head)
# @lc code=end

