# TAGS: Premium, Linked List
# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    # 404 ms, 86.50%. Time and Space: O(N)
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        rv = root = PolyNode()
        while poly1 or poly2:
            if None in (poly1, poly2):
                root.next = poly1 or poly2
                break
            
            if poly1.power > poly2.power:
                root.next = PolyNode(poly1.coefficient, poly1.power)
                poly1 = poly1.next
            elif poly1.power < poly2.power:
                root.next = PolyNode(poly2.coefficient, poly2.power)
                poly2 = poly2.next
            else:
                root.next = PolyNode(poly1.coefficient + poly2.coefficient, poly2.power)
                poly1 = poly1.next
                poly2 = poly2.next
            if root.next.coefficient:
                root = root.next
            else:
                root.next = None
        return rv.next
    
    # 404 ms, 86.50%. Time O(N). Space: O(1)
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        rv = root = PolyNode()
        while poly1 and poly2:
            if poly1.power > poly2.power:
                root.next = poly1
                poly1 = poly1.next
                
            elif poly1.power < poly2.power:
                root.next = poly2
                poly2 = poly2.next
                
            else:
                poly1.coefficient += poly2.coefficient
                root.next = poly1
                poly1 = poly1.next
                poly2 = poly2.next
                
            if root.next.coefficient:
                root = root.next
            else:
                root.next = None
        root.next = poly1 or poly2
        return rv.next