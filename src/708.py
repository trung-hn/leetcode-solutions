"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""
# TAGS: Premium, Linked List
class Solution:
    #  36 ms, 80%. Time: O(N). Space: O(1)
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            head = Node(insertVal)
            head.next = head
            return head
        
        if head.val > head.next.val:
            return self.at_largest_node(head, insertVal)
        
        node, fast = head, head
        largest, same = 0, None
        while node.val <= node.next.val:
            fast = fast.next.next
            node = node.next
            largest = max(largest, node.val)
            if fast is node: 
                same = True
                break

        # When all values are the same, we can insert anywhere
        if same: 
            node.next = Node(insertVal, node.next)
            return head
            
        # Find the largest node in the cycle
        while node.val <= node.next.val:
            node = node.next    
        
        return self.at_largest_node(node, insertVal)

    def at_largest_node(self, head, insertVal):
        node = head
        if insertVal >= node.val:
            node.next = Node(insertVal, node.next)
            return head
        
        while node.next.val < insertVal:
            node = node.next
        node.next = Node(insertVal, node.next)
        return head
