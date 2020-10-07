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
                
        
