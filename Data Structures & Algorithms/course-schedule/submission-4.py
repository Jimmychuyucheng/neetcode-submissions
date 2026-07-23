class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i : [] for i in range(numCourses)}

        # build the preMap
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        route = set()
        def dfs(crs):
            if crs in route:
                return False
            if preMap[crs] == []:
                return True
            
            route.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            
            #if pre all true, then...
            route.remove(crs)
            preMap[crs] = []
            return True

        for i in range(numCourses):
            if not dfs(i): return False
        return True


        