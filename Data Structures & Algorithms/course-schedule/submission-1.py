class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        visit = set()

        # build the crs:ore mapping adjacency list
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # black box to check whether it has a cycle (return false)
        # using visit add and remove to do the dfs and backtracking
        def dfs(crs):
            # base case
            if crs in visit:
                return False
            if preMap[crs] == []:
                return True

            # state transition
            visit.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            
            # backtracking
            visit.remove(crs)
            # memoization
            preMap[crs] == []
            return True

        # entry point traverse avery vertuces (since it may not be a connected graph)
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True



        