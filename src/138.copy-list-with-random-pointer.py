#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
# TAGS: Hash Table, Linked List
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    """
    O(1) Space Solution: https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43491/A-solution-with-constant-space-complexity-O(1)-and-linear-time-complexity-O(N)
    3 Step:
        - Create temp nodes between original nodes
        - Assign the pointers for random because we already know where they are
        - Seperate temp and original nodes and return the temp nodes
    """
    # 40 ms, 36.34%. Time and Space: O(N)
    def copyRandomList(self, head: 'Node') -> 'Node':
        ref = {}
        root = temp = Node(0)
        node = head
        while node: 
            temp.next = Node(node.val)
            ref[node] = temp.next
            temp = temp.next
            node = node.next         
        
        node = head
        while node: 
            if node.random:
                ref[node].random = ref[node.random]
            node = node.next
        
        return root.next
# @lc code=end

