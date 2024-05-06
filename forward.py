def forward_chaining(knowledge_base,goal):

    agenda=[goal]
    inferred=set()

    while agenda:
        current=agenda.pop(0)
        if current in inferred:
            continue
        if current not in knowledge_base:
            return False
        inferred.add(current)
        for st in knowledge_base[current]:
            agenda.append(st)
    return True

kb={
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['F'],
    'F': []
}

goal='F'

if forward_chaining(kb,goal):
    print(goal,"can be inferred from kb")
else:
    print(goal,"cannot be inferred from kb")