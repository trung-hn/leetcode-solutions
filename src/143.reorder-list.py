#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 92 ms, 90.72%. Time O(N). Space: O(1)
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return
        # Get len
        L = 0
        node = head
        while node:
            node = node.next
            L += 1
        L2 = L // 2
        L1 = L - L2

        # Move node to head2
        node = head
        prev = None
        for _ in range(L1):
            prev = node
            node = node.next
        prev.next = None
        
        # Get head1, head2
        head1 = head
        head2 = node
        def flip(node):
            prev = None
            while node:
                nxt = node.next
                node.next = prev
                prev = node
                node = nxt
            return prev
        head2 = flip(head2)

        # Reorder list
        rv = head1
        for _ in range(L1):
            if not head2: break
            n1 = head1.next
            n2 = head2.next
            head2.next = n1
            head1.next = head2
            head1 = n1
            head2 = n2
        return rv
        
    # Similar Complexity but much cleaner. From Solution
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return 
        
        # find the middle of linked list [Problem 876]
        # in 1->2->3->4->5->6 find 4 
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
            
        # reverse the second part of the list [Problem 206]
        # convert 1->2->3->4->5->6 into 1->2->3->4 and 6->5->4
        # reverse the second half in-place
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next       

        # merge two sorted linked lists [Problem 21]
        # merge 1->2->3->4 and 6->5->4 into 1->6->2->5->3->4
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
# @lc code=end

