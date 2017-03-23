class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        counter = 0
        self.row = len(grid)
        self.col = len(grid[0])
        for line in grid:
            line.append(0)
            line.insert(0,0)
        grid.insert(0, [0] * (self.col + 2))
        grid.append([0] * (self.col + 2))
        for i in xrange(1, self.row + 1):
            for j in xrange(1, self.col + 1):
                if grid[i][j] == 1:
                    counter += self.count(i, j, grid)
        return counter
        
        
    
    def count(self, i, j, grid):
        counter = 0
        if grid[i - 1][j] == 0:
            counter += 1
        if grid[i + 1][j] == 0:
            counter += 1
        if grid[i][j + 1] == 0:
            counter += 1
        if grid[i][j - 1] == 0:
            counter += 1
        return counter
            
        
        