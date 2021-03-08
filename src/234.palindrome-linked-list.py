#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# TAGS: Linked List, Two Pointers.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    # Time: O(N). Space: O(1)
    # Flip the first half and compare between 2 pointers
    def isPalindrome(self, head: ListNode) -> bool:
        def flip(node, counter):
            prev = None
            for _ in range(counter):
                nxt = node.next
                node.next = prev
                prev = node
                node = nxt
            return prev, node

        # Get length
        L = 1
        node = head
        while node.next:
            node = node.next
            L += 1

        # Flip first half
        head1, head2 = flip(head, L//2)
        if L % 2:
            head2 = head2.next

        # Compare between 2 halves
        while head1:
            if head1.val != head2.val:
                return False
            head1 = head1.next
            head2 = head2.next
        return True


# @lc code=end
