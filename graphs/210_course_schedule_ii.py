# 210. Course Schedule II
# https://leetcode.com/problems/course-schedule-ii/
# Difficulty: Medium
#
# There are numCourses courses labeled from 0 to numCourses - 1. You are given
# an array prerequisites where prerequisites[i] = [a, b] indicates that you must
# take course b first if you want to take course a.
#
#   - For example, the pair [0, 1] means to take course 0 you must first take
#     course 1.
#
# Return the ordering of courses you should take to finish all courses. If there
# are many valid answers, return any of them. If it is impossible to finish all
# courses (i.e. there is a cycle), return an empty array.
#
# Example 1:
#   Input:  numCourses = 2, prerequisites = [[1,0]]
#   Output: [0,1]
#   Explanation: Take course 0 first (no prereqs), then course 1.
#
# Example 2:
#   Input:  numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
#   Output: [0,1,2,3]  (or [0,2,1,3] — any valid topological order)
#
# Example 3:
#   Input:  numCourses = 1, prerequisites = []
#   Output: [0]
#
# Constraints:
#   1 <= numCourses <= 2000
#   0 <= prerequisites.length <= numCourses * (numCourses - 1)
#   prerequisites[i].length == 2
#   0 <= a, b < numCourses
#   a != b
#   All the pairs [a, b] are distinct.

from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = set()
        path = set()
        res = []

        prevMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prevMap[crs].append(pre)
        
        def dfs(crs):
            if crs in path:
                return False 
            if crs in visited:
                return True
            if prevMap[crs] == []:
                res.append(crs)
                visited.add(crs)
                return True
            path.add(crs)
            for pre in prevMap[crs]:
                if not dfs(pre):
                    return False
            path.remove(crs)
            res.append(crs)
            visited.add(crs)
            prevMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return res
    
        

            
            