class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        maxArea = 0

        def bfs(r, c):
            area = 1
            queue = collections.deque()
            visited.add((r,c))
            queue.append((r,c))
            while queue:
                row,col = queue.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    r = row+dr
                    c=col+dc
                    if (r) in range(rows) and (c) in range(cols) and grid[r][c]==1 and (r, c) not in visited:
                        area+=1
                        queue.append((r,c))
                        visited.add((r,c))
            return area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    maxArea = max(maxArea, bfs(i,j))

        return maxArea