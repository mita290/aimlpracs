graph = {
    '1' : ['2','3'],
    '2' : ['4','5'],
    '3' : ['6','7'],
    '4' : [],
    '5' : [],
    '6' : ['7'],
    '7' : [],
}

visited=[]
queue=[]

def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)

    while queue:
        m=queue.pop(0)
        print(m, end=" ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("BFS TRAVERSAL: ")
bfs(visited,graph,'1')