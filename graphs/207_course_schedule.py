# 207. Course Schedule
# https://leetcode.com/problems/course-schedule/
# Difficulty: Medium
#
# There are numCourses courses labeled from 0 to numCourses - 1. You are given
# an array prerequisites where prerequisites[i] = [a, b] indicates that you must
# take course b first if you want to take course a.
#
#   - For example, the pair [0, 1] means that to take course 0 you have to first
#     take course 1.
#
# Return true if you can finish all courses. Otherwise, return false.
#
# Example 1:
#   Input:  numCourses = 2, prerequisites = [[1,0]]
#   Output: true
#   Explanation: Take course 0 first, then course 1.
#
# Example 2:
#   Input:  numCourses = 2, prerequisites = [[1,0],[0,1]]
#   Output: false
#   Explanation: Courses 0 and 1 depend on each other — a cycle, impossible.
#
# Constraints:
#   1 <= numCourses <= 2000
#   0 <= prerequisites.length <= 5000
#   prerequisites[i].length == 2
#   0 <= a, b < numCourses
#   All the pairs prerequisites[i] are unique.

from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prevMap = {i : [] for i in range(numCourses)} #adj list
        for crs, pre in prerequisites:
            prevMap[crs].append(pre)
        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if prevMap[crs] == []:
                return True
            visited.add(crs)
            for pre in prevMap[crs]:
                if not dfs(pre): return False
            visited.remove(crs)
            preMap[crs] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True
