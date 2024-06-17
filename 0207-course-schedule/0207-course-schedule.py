class Solution:
    
        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = collections.defaultdict(list)
        
        
        
        for i in prerequisites:
            adj_list[i[1]].append(i[0])
        visited = set()
        
        def dfs(node):
            # while stack:
            #     num = stack.pop(0)
            #     visited[num] = True
            #     for i in adj_list[num]:
            #         if i not in visited:
            #             stack.insert(0,i)
            if node in visited:
                return False
            if adj_list[node]==[]:
                return True
            visited.add(node)
            for pre in adj_list[node]:
                if not dfs(pre): return False
            visited.remove(node)
            adj_list[node] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False
        return True

        
        
#         for i in adj_list:
        