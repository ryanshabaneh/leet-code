# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/
# Difficulty: Medium
#
# Given an m x n 2D binary grid which represents a map of '1's (land) and '0's
# (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all four edges of the grid are all
# surrounded by water.
#
# Example 1:
#   Input:  grid = [
#     ["1","1","1","1","0"],
#     ["1","1","0","1","0"],
#     ["1","1","0","0","0"],
#     ["0","0","0","0","0"]]
#   Output: 1
#
# Example 2:
#   Input:  grid = [
#     ["1","1","0","0","0"],
#     ["1","1","0","0","0"],
#     ["0","0","1","0","0"],
#     ["0","0","0","1","1"]]
#   Output: 3
#
# Constraints:
#   m == grid.length
#   n == grid[i].length
#   1 <= m, n <= 300
#   grid[i][j] is '0' or '1'.

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        row = len(grid)
        col = len(grid[0])

        def dfs(r,c):
            if (r >= len(grid) or c >= len(grid[0]) or r < 0 or c < 0):
                return
            
            if (r,c) in visited:
                return
            if grid[r][c] == "0":
                return
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) not in visited and grid[r][c] == "1":
                   count += 1
                   dfs(r,c)
        return count

#Time: O(m × n)
#Space: O(m × n)
#this was very fun new fav
    


        
