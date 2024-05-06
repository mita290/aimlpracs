from heapq import heappop, heappush
def heuristic(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def astar(grid,start,goal):
    open_set=[(0,start)]
    came_from={}
    g_score={start:0}

    while open_set:
        _, current=heappop(open_set)

        if current==goal:
            path=[]
            while current in came_from:
                path.append(current)
                current=came_from[current]
            path.append(start)
            return path[::-1]
        
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            neighbour=(current[0]+dx,current[1]+dy)
            
            if 0<=neighbour[0]<len(grid) and 0<=neighbour[1]<len(grid) and grid[neighbour[0]][neighbour[1]]!=1:
                tentative_g_score=g_score[current]+1

                if neighbour not in g_score or tentative_g_score < g_score[neighbour]:
                    came_from[neighbour]=current
                    g_score[neighbour]=tentative_g_score
                    f_score=tentative_g_score + heuristic(neighbour,goal)
                    heappush(open_set,(f_score,neighbour))
    return None

grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

start=(0,0)
goal=(4,4)

path=astar(grid,start,goal)
if path:
    print("Path found: ",path)
else:
    print("Path not found.")
