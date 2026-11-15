from collections import deque
class Node:
    def __init__(self, val : int, neighbors : list[Node]):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def nodeListCreator(self, numCourses : int):
        list1 = []
        for i in range(numCourses):
            list1.append(Node(i, []))
        return list1
    def isCyclic(self, nodes: list[Node], numCourses: int):
        indegree = [0] * numCourses
        for node in nodes:
            for neighbor in node.neighbors:
                indegree[neighbor.val] += 1
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        count = 0
        while q:
            curr = q.popleft()
            count += 1
            for neighbor in nodes[curr].neighbors:
                indegree[neighbor.val] -= 1
                if indegree[neighbor.val] == 0:
                    q.append(neighbor.val)
        return count != numCourses
    
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        listOfNodes = self.nodeListCreator(numCourses)
        for item in prerequisites:
            listOfNodes[item[0]].neighbors.append(listOfNodes[item[1]])
        return not self.isCyclic(listOfNodes, numCourses)
        