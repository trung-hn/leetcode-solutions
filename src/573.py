# TAGS: Premium, Math
class Solution:
    # 140 ms, 68.63%. Time: O(N). Space: O(1)
    # Try all position and find the smallest one
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        def get_distance(point1, point2):
            return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
        
        total_from_tree = 0
        for nut in nuts:
            total_from_tree += get_distance(nut, tree) * 2
            
        ans = float('inf')
        for nut in nuts:
            distance = total_from_tree - get_distance(nut, tree) + get_distance(squirrel, nut)
            ans = min(ans, distance)
        return ans
    
    # 148 ms, 39.22%. Time: O(N). Space: O(1)
    # Similar but 1 pass
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        def get_distance(point1, point2):
            return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
        
        ans = 0; d = float('-inf')
        for nut in nuts:
            ans += get_distance(nut, tree) * 2
            d = max(d, get_distance(nut, tree) - get_distance(squirrel, nut))
        return ans - d