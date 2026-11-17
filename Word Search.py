class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(x, y, i):
            # Out of bounds
            if x < 0 or x >= rows or y < 0 or y >= cols:
                return False

            # Wrong character or already visited
            if board[x][y] == "#" or board[x][y] != word[i]:
                return False

            # We found the entire word
            if i == len(word) - 1:
                return True

            # Mark as visited
            original = board[x][y]
            board[x][y] = "#"

            # Explore neighbors
            found = (
                dfs(x - 1, y, i + 1)
                or dfs(x + 1, y, i + 1)
                or dfs(x, y - 1, i + 1)
                or dfs(x, y + 1, i + 1)
            )

            # Backtrack
            board[x][y] = original

            return found

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True

        return False
