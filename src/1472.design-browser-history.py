#
# @lc app=leetcode id=1472 lang=python3
#
# [1472] Design Browser History
#

# @lc code=start
# TAGS: Design
class BrowserHistory:
    """
    Overall: Time and Space: O(1)
    224 ms, 99.16%
    """
    # Time and Space: O(1) 
    def __init__(self, homepage: str):
        self.curr = 0
        self.prev = 0
        self.history = [homepage]

    # Time and Space: O(1) 
    def visit(self, url: str) -> None:
        self.curr += 1
        self.prev = self.curr
        if len(self.history) <= self.curr:
            self.history.append(url)
        else:
            self.history[self.curr] = url

    # Time and Space: O(1) 
    def back(self, steps: int) -> str:
        self.curr = max(self.curr - steps, 0)
        return self.history[self.curr]
        
    # Time and Space: O(1) 
    def forward(self, steps: int) -> str:
        self.curr = min(self.curr + steps, self.prev)
        return self.history[self.curr]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
# @lc code=end

