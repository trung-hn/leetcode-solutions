"""
You are given two arrays of positive integers, boxes and warehouse, representing the heights of some boxes of unit width and the heights of n rooms in a warehouse respectively. The warehouse's rooms are labeled from 0 to n - 1 from left to right where warehouse[i] (0-indexed) is the height of the ith room.

Boxes are put into the warehouse by the following rules:

Boxes cannot be stacked.
You can rearrange the insertion order of the boxes.
Boxes can be pushed into the warehouse from either side (left or right)
If the height of some room in the warehouse is less than the height of a box, then that box and all other boxes behind it will be stopped before that room.
Return the maximum number of boxes you can put into the warehouse.
"""

# TAGS: Greedy, Premium
class Solution:
    # 720 ms, 76.70 %. Time: O(NlogN). Space: O(N)
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        from_left = [warehouse[0]]
        for space in warehouse[1:]:
            from_left.append(min(space, from_left[-1]))
        
        from_right = [warehouse[-1]]
        for space in reversed(warehouse[:-1]):
            from_right.append(min(space, from_right[-1]))
        
        adjusted_warehouse = []
        for i in range(len(from_left)):
            adjusted_warehouse.append(max(from_left[i], from_right[~i]))
        
        boxes.sort()
        adjusted_warehouse.sort()
        
        counter = i = j = 0
        while i < len(boxes) and j < len(adjusted_warehouse):
            if boxes[i] <= adjusted_warehouse[j]:
                counter += 1
                i += 1
            j += 1
        return counter
                
        
