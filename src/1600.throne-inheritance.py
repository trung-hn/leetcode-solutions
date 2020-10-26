#
# @lc app=leetcode id=1600 lang=python3
#
# [1600] Throne Inheritance
#

# @lc code=start
# TAGS: Tree, Design
class ThroneInheritance:
    # 752 ms, 90.45%
    def __init__(self, kingName: str):
        self.graph = collections.defaultdict(list)
        self.deaths = set()
        self.first_king = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName)

    def death(self, name: str) -> None:
        self.deaths.add(name)
        
    def getInheritanceOrder(self) -> List[str]:
        inheritance_order = []
        stack = [self.first_king]
        while stack:
            person = stack.pop()
            if person not in self.deaths:
                inheritance_order.append(person)
            stack.extend(self.graph[person][::-1])
        return inheritance_order

    # Similar to above but recursion. 
    def getInheritanceOrder(self) -> List[str]:
        def dfs(person, inheritance):
            if person not in self.deaths:
                inheritance.append(person)
            for child in self.graph[person]:
                dfs(child, inheritance)
                
        inheritance_order = []
        dfs(self.first_king, inheritance_order)
        return inheritance_order
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()




# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
# @lc code=end

