class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(city):
            for neighbor in range(len(isConnected)):
                if isConnected[city][neighbor] == 1 and neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
            
        num_provinces = 0
        visited = set()

        for city in range(len(isConnected)):
            if city not in visited:
                num_provinces+=1
                visited.add(city)
                dfs(city)
        
        return num_provinces
