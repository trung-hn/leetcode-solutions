#
# @lc app=leetcode id=1171 lang=python3
#
# [1171] Remove Zero Sum Consecutive Nodes from Linked List
#


# @lc code=start
# TAGS: Hash Table, Linked List
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Cleaner Code
    # Time and Space: O(N)
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0, head)
        node, prefix, seen = head, 0, {}
        while node:
            prefix += node.val
            if prefix in seen:
                # Detect the sum to 0 => trim the nodes and restart from head.
                seen[prefix].next = node.next
                node, prefix, seen = head, 0, {}
                continue
            seen[prefix] = node
            node = node.next
        return head.next

    # Slightly more optimize.
    # Instead of restarting from head, we delete dict. This requires OrderedDict()
    # Time and Space: O(N)
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0, head)
        node, prefix, seen = head, 0, collections.OrderedDict()
        while node:
            prefix += node.val
            last = seen.get(prefix, node)
            while prefix in seen:
                # delete last element in seen (everything seen between last <-> node)
                seen.popitem()
            seen[prefix] = last
            last.next = node.next
            node = node.next
        return head.next


# @lc code=end
