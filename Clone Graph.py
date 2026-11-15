class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        clones = {node: Node(node.val)}
        q = deque([node])

        while q:
            temp = q.popleft()

            for neighbor in temp.neighbors:

                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    q.append(neighbor)

                clones[temp].neighbors.append(clones[neighbor])

        return clones[node]