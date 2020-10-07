"""You are given two arrays of positive integers, boxes and warehouse, representing the heights of some boxes of unit width and the heights of n rooms in a warehouse respectively. The warehouse's rooms are labelled from 0 to n - 1 from left to right where warehouse[i] (0-indexed) is the height of the ith room.

Boxes are put into the warehouse by the following rules:

Boxes cannot be stacked.
You can rearrange the insertion order of the boxes.
Boxes can only be pushed into the warehouse from left to right only.
If the height of some room in the warehouse is less than the height of a box, then that box and all other boxes behind it will be stopped before that room.
Return the maximum number of boxes you can put into the warehouse.

 

Example 1:


Input: boxes = [4,3,4,1], warehouse = [5,3,3,4,1]
Output: 3
Explanation: 

We can first put the box of height 1 in room 4. Then we can put the box of height 3 in either of the 3 rooms 1, 2, or 3. Lastly, we can put one box of height 4 in room 0.
There is no way we can fit all 4 boxes in the warehouse."""

# TAGS: Greedy, Premium

class Solution:
    # 704 ms, 35.55 %. Time: O(NlogN) and Space: O(N)
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        usable_height = [warehouse[0]]
        prev = warehouse[0]
        for room in warehouse[1:]:
            if room <= prev:
                prev = room
            usable_height.append(prev)
        
        usable_height.reverse()        
        boxes.sort()
        
        i = cnt = 0
        for box in boxes:
            while i < len(usable_height) and box > usable_height[i]:
                i += 1
            if i < len(usable_height) and box <= usable_height[i]:
                i += 1
                cnt += 1
        return cnt

    # 640 ms, 89.7 %. Cleaner solution after doing 1580
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        usable_height = [warehouse[0]]
        for room in warehouse[1:]:
            usable_height.append(min(room, usable_height[-1]))
        
        usable_height.reverse()
        boxes.sort()
        
        i = j = cnt = 0
        while i < len(boxes) and j < len(usable_height):
            if boxes[i] <= usable_height[j]:
                cnt += 1
                i += 1
            j += 1
        return cnt
