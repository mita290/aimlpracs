graph = {
    '1' : ['2','3'],
    '2' : ['4','5'],
    '3' : ['6','7'],
    '4' : [],
    '5' : [],
    '6' : ['7'],
    '7' : [],
}

visited=set()

def dfs(visited,graph,node):
    if node not in visited:
        print(node,end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)
print("DFS: ")
dfs(visited,graph,'1')