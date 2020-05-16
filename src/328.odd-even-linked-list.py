#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# TAGS: Linked List
# REVIEWME:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 40 ms, 85.05%. O(N), O(1), Cleaner
    def oddEvenList(self, node: ListNode) -> ListNode:
        odd = ListNode(None)
        head_even = even = ListNode(None)
        i = 1
        while node:
            if i % 2:
                odd.next = node
                odd = odd.next
            else:
                even.next = node
                even = even.next
            node = node.next
            i += 1
        # Clean up tail
        odd.next = even.next = None
        # Connect odd to even
        odd.next = head_even.next
        return head
    
    # 40 ms, 85.05%. O(N), O(1), Cleaner
    def oddEvenList(self, node: ListNode) -> ListNode:
        head_odd = odd = ListNode(None)
        head_even = even = ListNode(None)
        while node:
            odd.next = node
            odd = odd.next
            even.next = node.next
            even = even.next
            node = node.next.next if even else None
        # Connect odd to even
        odd.next = head_even.next
        return head_odd.next
        
# @lc code=end

