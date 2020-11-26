# TAGS: Premium, String, Binary Search
# """
# This is FontInfo's API interface.
# You should not implement it, or speculate about its implementation
# """
#class FontInfo(object):
#    Return the width of char ch when fontSize is used.
#    def getWidth(self, fontSize, ch):
#        """
#        :type fontSize: int
#        :type ch: char
#        :rtype int
#        """
# 
#    def getHeight(self, fontSize):
#        """
#        :type fontSize: int
#        :rtype int
#        """
class Solution:
    # Without counter. 692 ms, 8.6%  Time: O(NlogN). Space: O(1)
    # With counter. 480 ms, 74.19%  Time: O(logN). Space: O(1)
    def maxFont(self, text: str, w: int, h: int, fonts: List[int], fontInfo : 'FontInfo') -> int:
        counter = collections.Counter(text)
        def fit_on_screen(font_size, text):
            width = sum(fontInfo.getWidth(font_size, c) * f for c, f in counter.items())
            height = fontInfo.getHeight(font_size)
            return width <= w and height <= h
        
        lo, hi = 0, len(fonts) - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if fit_on_screen(fonts[mid], text):
                lo = mid
            else:
                hi = mid - 1
                
        return fonts[lo] if fit_on_screen(fonts[lo], text) else -1