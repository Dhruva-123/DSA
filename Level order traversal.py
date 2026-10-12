##102. Binary Tree Level Order Traversal
#Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

#Input: root = [3,9,20,null,null,15,7]
#Output: [[3],[9,20],[15,7]]
#Example 2:

#Input: root = [1]
#Output: [[1]]
#Example 3:

#Input: root = []
#Output: []

from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        ans = []
        queue = deque([root])
        while queue:
            new_level = []
            for _ in range(len(queue)):
                item = queue.popleft()
                new_level.append(item.val)
                if item.left:
                    queue.append(item.left)
                if item.right:
                    queue.append(item.right)
            ans.append(new_level)
        return ans